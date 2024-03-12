#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.03
# modified date : 2024.03.03
# description   :

import mysql.connector as mysql_con

from libs.algorithm import library as algo_lib
import todo_list.constants as constants


@algo_lib.singleton
class DBTodolist:
    def __init__(self, user, passwd):
        try:
            self.connect = mysql_con.connect(
                host='192.168.5.55',
                port='3305',
                user=user,
                password=passwd,
                database='todo_db'
            )
            self.cursor = self.connect.cursor()
        except mysql_con.errors.ProgrammingError as err:
            print(err)
            self.connect = None
            self.cursor = None
            raise constants.CustomExcept(err, _user=user)

    def __del__(self):
        if (self.connect is not None) and self.is_connected_db():
            # self.cursor.close()
            self.connect.close()

    def is_connected_db(self) -> bool:
        return self.connect.is_connected()

    def get_todo_list(self):
        q = '''
        select id, todo, save_datetime, deadline, status, author_id from todo_list;
        '''
        self.cursor.execute(q)
        res = self.cursor.fetchall()
        return res

    def get_username_by_id(self, uid):
        q = '''
        select author from todo_author where id = %s;
        ''' % uid
        self.cursor.execute(q)
        res = self.cursor.fetchall()
        return res

    def get_todo_status(self):
        q = '''
        select * from todo_status;
        '''
        self.cursor.execute(q)
        res = list(map(lambda x: x[0], self.cursor.fetchall()))
        return res

    def get_id(self):
        return self.cursor.lastrowid

    def add_todo(self, data: list) -> bool:
        # ('home tra', '2023/12/15', '2023/12/31', 'inprogress', 3);
        assert isinstance(data, list)
        assert len(data) == 5
        q = '''
        INSERT INTO todo_list (todo, save_datetime, deadline, status, author_id) 
        VALUES (%s, %s, %s, %s, %s);
        '''
        try:
            self.cursor.execute(q, data)
            self.connect.commit()
            return True
        except Exception as err:
            self.connect.rollback()
            print(err)
            return False

    def del_todo(self, data_id: int) -> bool:
        q = '''
        DELETE FROM todo_list WHERE id=%s;
        ''' % data_id
        try:
            self.cursor.execute(q)
            self.connect.commit()
            return True
        except Exception as err:
            self.connect.rollback()
            print(err)
            return False

    def update_todo(self, data_id: int, ste: int) -> bool:
        q = '''
        UPDATE todo_list SET status = '%s' WHERE id = %s;
        ''' % (ste, data_id)
        try:
            self.cursor.execute(q)
            self.connect.commit()
            return True
        except Exception as err:
            self.connect.rollback()
            print(err)
            return False


if __name__ == '__main__':
    db_todo = DBTodolist()
    # for i in db_todo.get_todo_list():
    #     print(i)
    db_todo2 = DBTodolist()

    print(db_todo)
    print(db_todo2)

