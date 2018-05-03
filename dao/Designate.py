from util.DBHelper import DBHelper


class Designate():
    def __init__(self, db):
        self.db = db

    def designate_by_scholar(self, scholar_table, duty_table, data_table,
                             duty_out_table):
        db = DBHelper(self.db)
        conn = db.getConnection()
        cursor = conn.cursor()
        scholar_sql = "select id,name from {}".format(scholar_table)
        cursor.execute(scholar_sql)
        scholars = cursor.fetchall()

        # 删除指派表
        delete_sql = "delete from {}".format(duty_out_table)
        cursor.execute(delete_sql)
        conn.commit()

        for scholar in scholars:
            id = scholar['id']
            name = scholar['name']
            duty_sql = "insert into {} (sid,author,duty) select sid,author,duty from {} where sid in (select sid from {}) and author ='{}'".format(
                duty_out_table, duty_table, data_table, name)
            cursor.execute(duty_sql)
            conn.commit()
        # 找到没有指派过的
        not_designate_sql = "select sid from {} where sid not in (select sid from {})".format(
            data_table, duty_out_table)
        cursor.execute(not_designate_sql)
        sids = cursor.fetchall()
        print(len(sids))
        for sid_dict in sids:
            sid = sid_dict['sid']
            detail_one = "select * from {} where sid='{}'".format(
                data_table, sid)
            cursor.execute(detail_one)
            detail = cursor.fetchone()
            decription = detail['decription'] if detail['decription'] else ''
            title_cn = detail['title_cn'] if detail['title_cn'] else ''
            series = detail['series'] if detail['series'] else ''
            for scholar in scholars:
                id = scholar['id']
                name = scholar['name']
                if name in (decription+title_cn+series):
                        description_sql = "insert into {} (sid,author,duty) values ('{}','{}','{}')".format(duty_out_table,sid,name,'内容相关')
                        cursor.execute(description_sql)
                        conn.commit()
            # print(decription)
            # print(sid)
        # 找到没有指派过的
        not_designate_sql = "select sid from {} where sid not in (select sid from {})".format(
            data_table, duty_out_table)
        cursor.execute(not_designate_sql)
        sids = cursor.fetchall()
        print(len(sids))
        for sid_dict in sids:
            sid = sid_dict['sid']
            print(sid)
