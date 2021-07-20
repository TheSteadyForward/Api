# coding:utf-8

import logging
import traceback
import pymysql
from django.conf import settings

log = logging.getLogger(__name__)

CONFIG_INFO = settings.CONFIG_INFO


class DB():
    def __init__(self, mark):
        self.mark = mark

    def conn_db(self, db_name=""):
        """
        功能            建立pymysql连接
        -----------------------------------
        添加人          添加时间           作用
        -----------------------------------
        fxk            2018-01-04
        """
        if self.mark == "APP":
            DB_USER = CONFIG_INFO.get('DB_APP_TB_USER')
            DB_PASSWORD = CONFIG_INFO.get('DB_APP_TB_PASSWORD')
            DB_HOST = CONFIG_INFO.get('DB_APP_TB_HOST')
            DB_PORT = int(CONFIG_INFO.get('DB_APP_TB_PORT'))
        elif self.mark == "YEWU":
            DB_USER = CONFIG_INFO.get('DB_YEWU_USER')
            DB_PASSWORD = CONFIG_INFO.get('DB_YEWU_PASSWORD')
            DB_HOST = CONFIG_INFO.get('DB_YEWU_HOST')
            DB_PORT = int(CONFIG_INFO.get('DB_YEWU_PORT'))
        elif self.mark == "ZIYUAN":
            DB_USER = CONFIG_INFO.get('DB_ZIYUAN_USER')
            DB_PASSWORD = CONFIG_INFO.get('DB_ZIYUAN_PASSWORD')
            DB_HOST = CONFIG_INFO.get('DB_ZIYUAN_HOST')
            DB_PORT = int(CONFIG_INFO.get('DB_ZIYUAN_PORT'))
        else:
            return None

        return pymysql.connect(host=DB_HOST,
                               user=DB_USER,
                               port=DB_PORT,
                               password=DB_PASSWORD,
                               database=db_name,
                               charset="utf8")

    def exec_sql(self, db_name, sql, conn=None, close=True):
        """执行更新操作SQL"""
        if not sql:
            return
        if conn is None:
            conn = self.conn_db(db_name)
        cxn = conn.cursor()
        cxn.execute(sql)
        conn.commit()
        cxn.close()
        if close:
            conn.close()

    def exec_sql_statements(self, db_name, sql_statements, conn=None, close=True):
        """执行分号分隔的多条SQL"""
        if not sql_statements:
            return
        if conn is None:
            conn = self.conn_db(db_name)
        for sql in sql_statements.split(";"):
            sql = sql.strip()
            if not sql:
                continue
            cxn = conn.cursor()
            try:
                # 执行sql语句
                cxn.execute(sql)
                # 提交到数据库执行
                conn.commit()
            except:
                traceback.print_exc()
                # Rollback in case there is any error
                conn.rollback()
                continue

            # 关闭数据库连接
            cxn.close()
        if close:
            conn.close()

    def fetchone_sql(self, db_name, sql, conn=None, close=True):
        """
        查询SQL单条数据
        """
        if sql is None or sql == "":
            return
        if conn is None:
            conn = self.conn_db(db_name)
        cursor = conn.cursor()
        cursor.execute(sql)
        fetchone = cursor.fetchone()
        cursor.close()
        if close:
            conn.close()
        return fetchone

    def fetchall_sql(self, db_name, sql, conn=None, close=True):
        """返回查询结果"""
        if not sql:
            return
        if conn is None:
            conn = self.conn_db(db_name)
        cursor = conn.cursor()
        cursor.execute(sql)
        object_list = cursor.fetchall()
        cursor.close()
        if close:
            conn.close()
        return object_list

    def fetchall_to_dict(self, db_name, sql, conn=None, close=True):
        """返回字典对象结果"""
        if not sql:
            return
        if conn is None:
            conn = self.conn_db(db_name)
        cursor = conn.cursor()
        cursor.execute(sql)
        object_list = self.dictfetchall(cursor)
        cursor.close()
        if close:
            conn.close()
        return object_list

    def fetchall_by_columns(self, db_name, sql, columns, conn=None, close=True):
        """返回指定列名字结果"""
        if not sql:
            return
        if conn is None:
            conn = self.conn_db(db_name)
        cursor = conn.cursor()
        cursor.execute(sql)
        object_list = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        if close:
            conn.close()
        return object_list

    def dictfetchall(self, cursor):
        """Returns all rows from a cursor as a dict"""
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]


if __name__ == "__main__":
    """
    调用示例：
    from db import conn_zy2, fetchall_to_dict
    fetchall = fetchall_to_dict(test, sql)
    """
