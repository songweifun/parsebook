from util.DBHelper import DBHelper
import pymysql



class Designate():
    def __init__(self, db):
        self.db = db
        h = DBHelper(self.db)
        self.conn = h.getConnection()
        self.cursor = self.conn.cursor()

    def is_in_table(self, table, field, field_value):
        search_sql_pre = "select count(*) as count from {} where `{}`='{}'"
        search_sql = search_sql_pre.format(table, field, field_value)
        self.cursor.execute(search_sql)
        count = self.cursor.fetchone()['count']
        if count < 1:
            return True
        else:
            return False

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
                    description_sql = "insert into {} (sid, author, duty, description_plus) values ('{}','{}','{}','{}')".format(duty_out_table, sid, name, '', pymysql.escape_string(title_cn+series+e200+c200+i200+f200+g200+subject_plus))
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

    def take_master_book(self, master_table, duty_table, from_table, target_table):
        master_sql =  "select name from {}".format(master_table)
        self.cursor.execute(master_sql)
        maters = self.cursor.fetchall()

        for master in maters:
            name = master['name']
            duty_sql = "select sid from {} where author= '{}'".format(duty_table,name)
            self.cursor.execute(duty_sql)
            dutys = self.cursor.fetchall()
            fgsql = "select sid from {} where f200 like '%{}%' or g200 like '%{}%'".format(from_table,name,name)
            self.cursor.execute(fgsql)
            fgs = self.cursor.fetchall()
            for duty in dutys:
                sid = duty['sid']
                if self.is_in_table(target_table, 'sid', sid):
                    insert_sql = "insert into {} select * from {} where sid ='{}'".format(target_table,from_table,sid)
                    self.cursor.execute(insert_sql)
                    self.conn.commit()
            for fg in fgs:
                sid = duty['sid']
                if self.is_in_table(target_table, 'sid', sid):
                    insert_sql = "insert into {} select * from {} where sid ='{}'".format(target_table,from_table,sid)
                    self.cursor.execute(insert_sql)
                    self.conn.commit()
        self.cursor.close()
        self.conn.close()