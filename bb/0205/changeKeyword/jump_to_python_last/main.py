import sys
import time
import shutil
import pathlib

from PySide2 import QtWidgets, QtCore

import cpy_ui

__import__('importlib').reload(cpy_ui)


class MultipleData:
    def __init__(self, data: dict, is_copied: bool):
        self.data = data
        self.is_copied = is_copied


# QtCore.QObject 클래스는 Qt의 가장 최상위 베이스 클래스
# 이것을 상속받아야만 connect를 사용할 수 있다.
class Signals(QtCore.QObject):
    # progress bar update
    sig_update = QtCore.Signal(int)
    # copy information
    sig_info = QtCore.Signal(MultipleData)


# QThread를 상속받아서 UI 벽돌이 되는 것을 방지
# 공유 객체를 사용하면 문제 발생되는 코드다.
class WorkThread(QtCore.QThread):
    def __init__(self, srcdir: pathlib.Path, dstdir: pathlib.Path):
        super().__init__()
        self.signals = Signals()
        self.__srcdir = srcdir
        self.__dstdir = dstdir
        self.is_stop = False

    def set_stop_attr(self, flag):
        self.is_stop = flag

    def run(self):
        # source 디렉토리의 모든 파일들
        filelst = list(self.__srcdir.glob('*'))
        # 프로그레스를 위한 변수 (0~1 숫자를 만들기 위한)
        totalcnt = len(filelst)

        for i, f in enumerate(filelst):
            # 0~1 까지의 숫자를 곱하기 100 해서 최종적으로 0~100으로 되게끔
            ratio = int((i / (totalcnt-1)) * 100)
            dst_fpath = self.__dstdir / f.name

            info = {'src_path': f.as_posix(),
                    'dst_path': dst_fpath.as_posix()}

            multi = MultipleData(info, False)

            # 목적지 디렉토리에 파일이 있으면 emit 발생시키고, 건너뜀.
            if dst_fpath.exists():
                self.signals.sig_info.emit(multi)
                continue
            else:
                try:
                    shutil.copy2(f.as_posix(), dst_fpath.as_posix())
                    # is_copied는 복사가 정말 이뤄졌는지 확인 용도
                    multi.is_copied = True
                except Exception:
                    multi.is_copied = False
                self.signals.sig_info.emit(multi)

            # progress를 위한 발생 시그널
            self.signals.sig_update.emit(ratio)

            time.sleep(1)

            # 복사 진행 중 멈춤을 위한 코드
            if self.is_stop:
                print('index:', i)
                break
        print('break 걸렸음')


class CopyUI(QtWidgets.QWidget, cpy_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.textEdit.setReadOnly(True)

        srcdir = pathlib.Path('/data/_test_src')
        dstdir = pathlib.Path('/home/rapa/workspace/_test_dst')

        self.work_thread = WorkThread(srcdir, dstdir)
        # 부모 프로세스가 종료되면 자식 스레드 함께 종료
        self.work_thread.setDaemon = True

        self.pushButton__start.clicked.connect(self.slot_start)
        self.pushButton__stop.clicked.connect(self.slot_stop)
        self.work_thread.signals.sig_update.connect(self.slot_update_progress)
        self.work_thread.signals.sig_info.connect(self.slot_info)

    @QtCore.Slot(MultipleData)
    def slot_info(self, info: MultipleData):
        if not info.is_copied:
            self.textEdit.append(f'복사되지 않은 파일: {info.data.get("src_path")}')
            self.textEdit.append('-' * 30)
        else:
            self.textEdit.append(
                f'{info.data.get("src_path")} -> {info.data.get("dst_path")}')

    @QtCore.Slot(int)
    def slot_update_progress(self, val):
        self.progressBar.setValue(val)

    def slot_start(self):
        # 스레딩 작업이 진행중이지 않으면
        if not self.work_thread.isRunning():
            self.work_thread.start()

    def slot_stop(self):
        if self.work_thread.isRunning():
            self.work_thread.set_stop_attr(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cpy = CopyUI()
    cpy.show()
    sys.exit(app.exec_())
