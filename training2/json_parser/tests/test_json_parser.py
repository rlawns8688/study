#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.05
# modified date : 2024.03.05
# description   :
import orjson
import pytest
import pathlib

from libs.utility import utils

from training2.json_parser.json_parser import JsonParser


# * -------------------- unit test functions ---------------------- * #
@pytest.fixture(scope='module')
def json_parser() -> JsonParser:
    root_dirpath = pathlib.Path(__file__).parent
    return JsonParser(pathlib.Path(root_dirpath / 'test.json'))


@utils.print_string_void
def test_one_dimension_keys_array_to_data() -> None:
    key_lst = ['root', '0', 'aaa']
    key_data = JsonParser.one_dimension_keys_array_to_data(key_lst, [{'aa': 1234, 'bb': 5555}, {'cc': 3333}])
    print(key_data)
    assert key_data == {'root': {'0': {'aaa': [{'aa': 1234, 'bb': 5555}, {'cc': 3333}]}}}


@utils.print_string_void
def test_data_to_one_dimension_keys_array() -> None:
    key_lst = ['root', '0', 'aaa']
    key_data = JsonParser.one_dimension_keys_array_to_data(key_lst, [{'aa': 1234, 'bb': 5555}, {'c': 3333}])
    data_lst = JsonParser.data_to_one_dimension_keys_array(key_data)
    print(data_lst)
    assert data_lst == ['root', '0', 'aaa']


@utils.print_string_void
def test_new_data() -> None:
    key_lst = ['root', '0', 'aaa']
    dat = JsonParser.new_data(key_lst, {'aa': 1234, 'bb': 5555})
    print(dat)
    assert dat == {'root': {'0': {'aaa': {'aa': 1234, 'bb': 5555}}}}


@utils.print_string_void
def test_get_has_null_value_data(json_parser) -> None:
    json_data = json_parser.json_data()
    print(JsonParser.get_has_null_value_data(json_data))
    assert JsonParser.get_has_null_value_data(json_data) == [{'bbb': None}]


@utils.print_string_void
def test_is_has_key(json_parser) -> None:
    json_data = json_parser.json_data()
    key_lst = ['root', '0', 'aaa', 'bbb']
    key_data = JsonParser.one_dimension_keys_array_to_data(key_lst)
    print(JsonParser.is_has_key(data=json_data, key_data=key_data))
    assert JsonParser.is_has_key(data=json_data, key_data=key_data) is True


@utils.print_string_void
def test_is_exists_key_list() -> None:
    find_key_lst = ['a', 'b', 'c', 'd']
    dest_key_lst = ['a', 'b', 'c']
    print(JsonParser.is_exists_key_list(find_key_lst, dest_key_lst))
    assert JsonParser.is_exists_key_list(find_key_lst, dest_key_lst) is False


@utils.print_string_void
def test_insert_item_to_data(json_parser) -> None:
    key_lst = ['root', '0', 'aaa', 'bbb', 'ccc']
    insert_data = JsonParser.one_dimension_keys_array_to_data(key_lst)
    print('insert data:', insert_data)

    json_data = json_parser.json_data()
    #
    print(json_data)
    inserted_cnt = JsonParser.insert_item_to_data(json_data, insert_data)
    print('inserted count: ', inserted_cnt)
    print(json_data)

    key_lst = ['root', '0', 'aaa', 'bbb']
    insert_data = JsonParser.one_dimension_keys_array_to_data(key_lst, ['gggg'])
    inserted_cnt = JsonParser.insert_item_to_data(json_data, insert_data)
    insert_data = JsonParser.one_dimension_keys_array_to_data(key_lst, ['123413'])
    inserted_cnt = JsonParser.insert_item_to_data(json_data, insert_data)
    print('inserted count: ', inserted_cnt)
    print(json_data)
    assert json_data == {'root': {'0': {'aaa': {'bbb': ['123413', 'gggg']}}}}


@utils.print_string_void
def test_remove_item_in_data(json_parser) -> None:
    json_data = json_parser.json_data()
    assert json_data == {'root': {'0': {'aaa': {'bbb': None}}}}
    key_lst = ['root', '0', 'aaa', 'bbb', 'ccc']
    remove_key_data = JsonParser.one_dimension_keys_array_to_data(key_lst)
    assert remove_key_data == {'root': {'0': {'aaa': {'bbb': {'ccc': None}}}}}

    inserted_num = JsonParser.insert_item_to_data(json_data, {'root': {'0': {'aaa': {'bbb': {'ccc': [5, 7]}}}}})
    assert json_data == {'root': {'0': {'aaa': {'bbb': {'ccc': [5, 7]}}}}}

    print('remove_key_data: ', remove_key_data)
    print(json_data)
    del_cnt = JsonParser.remove_item_in_data(json_data, remove_key_data)
    print('deleted count: ', del_cnt)
    print(json_data)
    assert json_data == {'root': {'0': {'aaa': {'bbb': None}}}}


@utils.print_string_void
def test_multi_data_to_two_dimension_key_array(json_parser) -> None:
    json_data = json_parser.json_data()
    collect_lst = list()
    JsonParser.multi_data_to_two_dimension_key_array(json_data, collect_lst)
    print(collect_lst)
    assert collect_lst == [['root'], ['root', '0'], ['root', '0', 'aaa'], ['root', '0', 'aaa', 'bbb']]


@utils.print_string_void
def test_change_category_name_from_data(json_parser) -> None:
    json_data = json_parser.json_data()
    change_key_lst = ['root', '0', 'aaa', 'bbb']
    print(json_data)
    assert json_data == {'root': {'0': {'aaa': {'bbb': None}}}}
    is_changed = JsonParser.change_category_name_from_data(
        data=json_data, key_lst=change_key_lst, new_cate_name='NEW_NAME')
    print(json_data)
    assert json_data == {'root': {'0': {'aaa': {'NEW_NAME': None}}}}
    print('is_changed: ', is_changed)
    assert is_changed is True


@utils.print_string_void
def test_get_value_in_data(json_parser) -> None:
    json_data = json_parser.json_data()
    key_lst = ['root', '0', 'aaa']
    key_data = JsonParser.one_dimension_keys_array_to_data(key_lst)
    print('key_data: ', key_data)
    assert key_data == {'root': {'0': {'aaa': None}}}
    result = json_parser.get_value_in_data(json_data, key_data)
    print('get value: ', len(result), result)
    assert len(result) == 1
    assert result == [{'bbb': None}]


if __name__ == '__main__':
    pass
