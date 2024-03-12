#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.05
# modified date : 2024.03.05
# description   :


import os
import sys
import typing
import bisect

import orjson
import pathlib

from libs.system import library as sys_lib
from libs.utility import utils


class Json(object):
    def __init__(self, json_filepath: pathlib.Path) -> None:
        self.__json_filepath = json_filepath

    def __str__(self) -> str:
        return self.__json_filepath.as_posix()

    @property
    def json_filepath(self) -> pathlib.Path:
        return self.__json_filepath

    def dump_json_file(self, data: typing.Dict) -> bool:
        try:
            sys_lib.System.save_json_file(self.json_filepath, data)
            return True
        except orjson.JSONDecodeError as err:
            sys.stderr.write(repr(err))
            return False

    def load_json_file(self, err_rm_file: bool = False) -> typing.Dict:
        try:
            try:
                return sys_lib.System.load_json_file(self.json_filepath)
            except ValueError as err:
                # 옵션이 켜져있고 value error가 발생한다면 삭제
                if err_rm_file:
                    if self.json_filepath.exists():
                        os.remove(self.json_filepath.as_posix())
                        return dict()
        except orjson.JSONDecodeError as err:
            sys.stderr.write(repr(err))
            return dict()

    # default json bytes 파일 생성
    def create_default_json_file(self) -> bool:
        if self.json_filepath.exists():
            sys.stderr.write('{0} 파일이 이미 존재합니다.'.format(self.json_filepath.as_posix()))
            return False
        default_data = {'root': None}
        self.dump_json_file(default_data)
        return True


class JsonParser(Json):
    def __init__(self, json_filepath: pathlib.Path) -> None:
        super(JsonParser, self).__init__(json_filepath)
        if not json_filepath.exists():
            sys.stderr.write('{0} json 파일을 찾을 수 없습니다.'.format(json_filepath.as_posix()))
            self.create_default_json_file()

    def json_data(self) -> typing.Dict:
        return self.load_json_file()

    def json_data_by_model_idx(self, model_idx: int) -> typing.Dict:
        jdata = self.json_data().get('root')
        if jdata is None:
            return dict()
        model_data = jdata.get(str(model_idx))
        return model_data if model_data is not None else dict()

    def json_items(self, json_data: typing.Dict) -> typing.List:
        if isinstance(json_data, list):
            return json_data
        data_lst = list()
        for key, val in json_data.items():
            if isinstance(val, list):
                data_lst.extend(val)
            else:
                data_lst.extend(self.json_items(json_data=val))
        return data_lst

    @staticmethod
    def get_count_model_index(json_data: typing.Dict) -> int:
        if not len(json_data):
            return 0
        model_indexes = json_data.get('root')
        if model_indexes is None:
            return 0
        return len(model_indexes)

    @staticmethod
    def get_index_list(json_data: typing.Dict) -> typing.List[int]:
        if not len(json_data):
            return list()
        model_indexes: typing.Dict = json_data.get('root')
        if model_indexes is None:
            return list()
        return list(sorted(map(lambda x: int(x), model_indexes.keys())))

    @staticmethod
    def one_dimension_keys_array_to_data(key_lst: typing.List, add_item: object = None, depth: int = 0) -> typing.Dict:
        if isinstance(key_lst, list):
            try:
                key = key_lst[depth]
                if isinstance(key, dict):
                    return key
                val = [JsonParser.one_dimension_keys_array_to_data(key_lst, add_item, depth + 1)]
                if val[0] is None:
                    if add_item is not None:
                        if isinstance(add_item, list):
                            val = [add_item]
                        else:
                            val = [[add_item]]
                    else:
                        val = [None]
                return dict(zip([key], val))
            except IndexError as err:
                pass

    @staticmethod
    def data_to_one_dimension_keys_array(data: typing.Dict) -> typing.List:
        if isinstance(data, dict):
            key_lst = list(data.keys())
            res_lst = list(map(lambda x: JsonParser.data_to_one_dimension_keys_array(x), data.values()))[0]
            if res_lst is None:
                res_lst = list()
            return key_lst + res_lst

    @staticmethod
    def new_data(key_lst: typing.List, child_item: typing.Dict) -> typing.Dict:
        if child_item is not None:
            key_lst.append(child_item)
        data = JsonParser.one_dimension_keys_array_to_data(key_lst)
        return data

    @staticmethod
    def get_has_null_value_data(data: typing.Dict) -> typing.List:
        lst = list()
        if isinstance(data, dict):
            for key, val in data.items():
                if data.get(key) is None:
                    return [data]
                return lst + JsonParser.get_has_null_value_data(val)

    @staticmethod
    def is_exists_key_list(find_key_lst: typing.List, dest_key_lst: typing.List) -> bool:
        if not isinstance(find_key_lst, list):
            find_key_lst = [find_key_lst]
        if not isinstance(dest_key_lst, list):
            dest_key_lst = [dest_key_lst]
        return all(
            map(lambda key: key in dest_key_lst, (key for key in find_key_lst)))

    @staticmethod
    def is_has_key(data: typing.Dict, key_data: typing.Dict) -> bool:
        bool_lst = list()
        if key_data is None:
            return True
        if not isinstance(data, dict):
            return False
        for key, val in key_data.items():
            bool_lst.append(key in data)
            get_data = data.get(key)
            bool_lst.append(JsonParser.is_has_key(get_data, val))
        return all(bool_lst)

    @staticmethod
    def get_value_in_data(data: typing.Dict, key_data: typing.Dict) -> typing.List:
        lst = list()
        if (not len(key_data)) or data is None:
            return list()
        find_key = list(key_data.keys())[0]
        find_val = key_data.get(find_key)
        if find_val is None:
            val = data.get(find_key)
            if val is None:
                return list()
            lst.append(val)
            return lst
        else:
            return JsonParser.get_value_in_data(data.get(find_key), find_val)

    @staticmethod
    def remove_item_in_data(data: typing.Dict, remove_key_data: typing.Dict) -> int:
        deleted_item = 0
        if isinstance(data, dict) and isinstance(remove_key_data, dict):
            remove_data_key = list(remove_key_data.keys())[0]
            remove_data_val = remove_key_data.get(remove_data_key)
            if remove_data_val is not None:
                deleted_item = JsonParser.remove_item_in_data(data.get(remove_data_key), remove_data_val)
            else:
                try:
                    del data[remove_data_key]
                    return 1
                except KeyError as err:
                    return 0
            # 자식 데이터가 하나도 없는 것은 null을 갖도록
            for item in data.items():
                _key, _val = item
                if (isinstance(_val, dict) or isinstance(_val, list)) and (len(_val) == 0):
                    data[_key] = None
        elif isinstance(data, list):
            for i in remove_key_data:
                if i in data:
                    data.remove(i)
                    deleted_item += 1
            if not len(data):
                print(data, type(data))
        return deleted_item

    @staticmethod
    def insert_item_to_data(data: typing.Dict, insert_data: typing.Dict) -> int:
        inserted_item = 0
        if isinstance(insert_data, dict):
            for key, val in insert_data.items():
                if data.get(key) is None:
                    data.update(insert_data)
                    inserted_item = 1
                else:
                    inserted_item = JsonParser.insert_item_to_data(data.get(key), val)
                    if not isinstance(val, dict):
                        if isinstance(data.get(key), list):
                            if isinstance(val, list):
                                for i in val:
                                    if i not in data.get(key):
                                        bisect.insort_right(data.get(key), i)
                                        inserted_item += 1
                            else:
                                if val not in data.get(key):
                                    bisect.insort_right(data.get(key), val)
                                    inserted_item = 1
                        else:
                            if data != insert_data:
                                data.update(insert_data)
                                inserted_item = 1
        return inserted_item

    @staticmethod
    def change_category_name_from_data(
            data: typing.Dict, key_lst: typing.List[str], new_cate_name: str) -> bool:
        flag = True
        if not len(key_lst):
            return False
        for key in key_lst:
            get_data = data.get(key)
            if isinstance(get_data, dict):
                flag &= JsonParser.change_category_name_from_data(get_data, key_lst[1:], new_cate_name)
        if len(key_lst) == 1:
            key = key_lst[0]
            if key in list(data.keys()):
                data[new_cate_name] = data.get(key)
                del data[key]
                flag = True
            else:
                flag = False
        return flag

    @staticmethod
    def multi_data_to_two_dimension_key_array(
            data: typing.Dict, collect_lst: typing.List, tmp_lst: typing.List = ()) -> None:
        lst = list()
        if isinstance(data, dict):
            for key, val in data.items():
                if val == 'root':
                    continue
                lst.extend(tmp_lst)
                lst.append(key)
                tmp_lst = list()
                collect_lst.append(lst[:])
                JsonParser.multi_data_to_two_dimension_key_array(val, collect_lst, lst)
                lst.remove(key)

    @staticmethod
    def collect_data(data, insert_data: typing.Dict) -> None:
        if isinstance(insert_data, dict):
            if not len(data):
                data.update(insert_data)
                return
            for key, val in insert_data.items():
                get_data = data.get(key)
                if get_data is None:
                    data.update(insert_data)
                else:
                    if isinstance(get_data, list):
                        pass
                    else:
                        JsonParser.collect_data(get_data, val)


if __name__ == '__main__':
    pass
