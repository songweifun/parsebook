from util.DBHelper import DBHelper
from util.TraSim.TraSim import Tra2Sim
import pymysql


class UpdateField():
    def __init__(self, db, table):
        self.db = db
        self.table = table

    def update_isbn(self, keys):
        db = DBHelper(self.db)
        conn = db.getConnection()
        cursor = conn.cursor()
        sql = "select * from {}".format(self.table)
        cursor.execute(sql)
        results = cursor.fetchall()
        update_keys = keys
        update_sql_pre = "update {} {} where id = '{}'"
        for result in results:
            u_str = 'set '
            for key in update_keys:
                f_v = result[key].replace('-', '')
                f_v = pymysql.escape_string(f_v)
                u_str += ("`" + key + "`" + '=' + "'" + f_v + "'" + ',')
            update_sql = update_sql_pre.format(self.table, u_str.strip(","),
                                               result['id'])
            print(update_sql)
            cursor.execute(update_sql)
            conn.commit()

    def update_type_cluster(self, form_type):
        db = DBHelper(self.db)
        conn = db.getConnection()
        cursor = conn.cursor()
        sql = "select * from {}".format(self.table)
        cursor.execute(sql)
        results = cursor.fetchall()
        update_sql_pre = "update {} set `type_cluster` = '{}' where id = '{}'"
        for result in results:
            if form_type == 'fdu':
                update_sql = update_sql_pre.format(self.table, result['type'],
                                                   result['id'])
            else:
                if '论文' in result['type'] or result['type'] == '博士后报告' or result['type'] == '':
                    result['type'] = 'XL'
                elif '古籍' in result['type'] or result['type'] == ['善本']:
                    result['type'] = 'AB'
                elif result['type'] == '期刊':
                    result['type'] = 'SE'
                else:
                    result['type'] = 'BK'
                update_sql = update_sql_pre.format(self.table, result['type'],
                                                   result['id'])

            print(update_sql)
            cursor.execute(update_sql)
            conn.commit()

        cursor.close()
        conn.close()
