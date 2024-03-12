from json_parser import json_parser

import pathlib
class TestJsonAPI:
    def __init__(self):
        test_json = pathlib.Path.home() / 'testapi.json'
        self.__japi = json_parser.JsonParser(test_json)

        data = self.__japi.new_data([
                    '/','aa','zz'
                ],
            {'aaa': 1234, 'aaad':22},
        )
        print(data)
        self.__japi.dump_json_file(data)
        # rm_keydata = self.__japi.one_dimension_keys_array_to_data(['/'])
        # self.__japi.remove_item_in_data(data, rm_keydata)
        # self.__japi.dump_json_file(data)
        # print(data)

if __name__ == '__main__':
    japi = TestJsonAPI()

