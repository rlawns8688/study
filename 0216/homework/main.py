


#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.16
# modified date  :   2024.02.16
# description  :

import site
site.addsitedir('/home/rapa/study')
from PySide2 import QtWidgets, QtCore, QtGui
import os, sys
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import music_alarm_ui
import random




class MusicAlarmUI(QtWidgets.QMainWindow, music_alarm_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


        self.webEngineView.resize(400, 300)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_lcdNumber)
        self.pushButton__start.clicked.connect(self.start_timer)

    def start_timer(self):
        time_str = self.lineEdit__timerStart.text()  # lineEdit__timerStart 위젯의 입력값 가져오기
        time_sec = int(time_str)  # 입력값을 정수형으로 변환

        self.lcdNumber.display(time_sec)  # lcdNumber 위젯에 초기값 설정
        self.timer.start(1000)  # 1초마다 update_lcdNumber 메소드 호출

    def update_lcdNumber(self):
        current_time = self.lcdNumber.value()  # 현재 lcdNumber 위젯의 값 가져오기

        if current_time > 0:
            self.lcdNumber.display(current_time - 1)  # 1초씩 감소
        else:
            self.timer.stop()  # 시간이 0이 되면 타이머 정지
            self.handle_get_items()
    def resize_webEngineView(self):
        # pass
        # UI의 크기에 맞게 webEngineView의 크기를 조정
        self.webEngineView.setGeometry(0, 0, self.ui.centralwidget.width(), self.ui.centralwidget.height())
    def handle_get_items(self):
        playlist_url = self.lineEdit__URL.text()  # lineEdit_URL 위젯의 입력값 가져오기
        playlist_id = self.extract_playlist_id(playlist_url)  # 플레이리스트 URL에서 ID 추출

        video_urls = self.get_playlist_items(playlist_id)
        random_video_url = random.choice(video_urls)

        self.get_playlist_items(playlist_id)  # 추출한 플레이리스트 ID를 인자로 get_playlist_items 함수 호출
        #
        self.webEngineView.load(QtCore.QUrl(random_video_url))
        self.webEngineView.show()

    def get_playlist_items(self, playlist_id):
        # 유튜브 API 클라이언트 빌드
        youtube = build('youtube', 'v3', developerKey='AIzaSyAgV1ieURSdPWGizkI6QMHYnRca46lna1o')  # 자신의 유튜브 API 키로 대체해주세요

        # playlistItems() 메소드를 사용하여 플레이리스트 아이템 가져오기
        response = youtube.playlistItems().list(
            part='snippet',
            maxResults=50,  # 최대 50개의 아이템 가져오기
            playlistId=playlist_id
        ).execute()

        video_urls = []

        # 가져온 플레이리스트 아이템을 처리하여 비디오 URL을 저장
        for item in response['items']:
            video_title = item['snippet']['title']
            video_id = item['snippet']['resourceId']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            video_urls.append(video_url)
            # embed_code = response['items'][0]['player']['embedHtml']

        return video_urls

    def extract_playlist_id(self, url):
        # 플레이리스트 URL에서 ID 추출
        playlist_id = None
        if 'list=' in url:
            playlist_id = url.split('list=')[1]
            if '&' in playlist_id:
                playlist_id = playlist_id.split('&')[0]
        return playlist_id


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    ui = MusicAlarmUI()
    ui.show()
    sys.exit(app.exec_())

