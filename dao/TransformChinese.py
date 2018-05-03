from util.DBHelper import DBHelper
from util.TraSim.TraSim import Tra2Sim
import pymysql


class TransformChinese():
    def __init__(self, db, table):
        self.db = db
        self.table = table

    def go(self, keys):
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
                f_v = Tra2Sim(result[key]).strip("'") if result[key] else ''
                f_v = pymysql.escape_string(f_v)
                u_str += ("`"+key+"`" + '=' + "'" + f_v + "'" + ',')
                # value_str += ("'" + pymysql.escape_string(f_v) + "'" + ',')
            update_sql = update_sql_pre.format(self.table, u_str.strip(","),
                                               result['id'])

            # print(update_sql)

            # # update_sql="update {} {} values {}".format(self.table,)
            # # 有问题待优化
            # for k, v in result.items():
            #     # if k not in ('id', 'title_py','title_for','title_foreign'):
            #     if k in update_keys:
            #         v = Tra2Sim(v).strip("'")
            #         update_sql = "update {} set {} = '{}' where id = '{}'".format(
            #             self.table, k, pymysql.escape_string(v), result['id'])
            #         cursor.execute(update_sql)
            #         print(update_sql)
            #         conn.commit()
            print(update_sql)
            cursor.execute(update_sql)
            conn.commit()
        cursor.close()
        conn.close()
