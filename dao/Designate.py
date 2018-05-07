from util.DBHelper import DBHelper
import pymysql



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
            description = detail['description'] if detail['description'] else ''
            description_plus = detail['description_plus'] if detail['description_plus'] else ''
            title_cn = detail['title_cn'] if detail['title_cn'] else ''
            series = detail['series'] if detail['series'] else ''
            e200 = detail['e200'] if detail['e200'] else ''
            c200 = detail['c200'] if detail['c200'] else ''
            i200 = detail['i200'] if detail['i200'] else ''
            f200 =  detail['f200'] if detail['f200'] else ''
            g200 =  detail['g200'] if detail['g200'] else ''
            subject_plus =  detail['subject_plus'] if detail['subject_plus'] else ''
            for scholar in scholars:
                id = scholar['id']
                name = scholar['name']
                if name in description_plus:
                    description_sql = "insert into {} (sid, author, duty, description_plus) values ('{}','{}','{}','{}')".format(duty_out_table, sid, name, '', pymysql.escape_string(description_plus))
                    cursor.execute(description_sql)
                    conn.commit()
                elif name in (title_cn+series+e200+c200+i200+f200+g200+subject_plus):
                    print(sid,title_cn+series+e200+c200+i200+f200+g200)
                    description_sql = "insert into {} (sid, author, duty, description_plus) values ('{}','{}','{}','{}')".format(duty_out_table, sid, name, '内容相关', pymysql.escape_string(title_cn+series))
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
