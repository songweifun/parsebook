from util.DBHelper import DBHelper


class Uncorrelated():
    def __init__(self, db):
        self.db = db

    def go(self, table, duty_table, scholar_table):
        db = DBHelper(self.db)
        conn = db.getConnection()
        cursor = conn.cursor()
        search_sql = "select sid from {}".format(table)
        cursor.execute(search_sql)
        sids = cursor.fetchall()
        print(len(sids))
        for sid_dic in sids:
            sid = sid_dic['sid']
            search_duty_sql = "select author from {} where sid = '{}'".format(
                duty_table, sid)
            cursor.execute(search_duty_sql)
            authors = cursor.fetchall()
            is_relation = False
            for author_dic in authors:
                author = author_dic['author']
                search_relation_sql = "select count(*) as count from {} where name = '{}'".format(
                    scholar_table, author)
                cursor.execute(search_relation_sql)
                count_dic = cursor.fetchone()
                count = count_dic['count']
                # print(count)
                if count > 0:
                    is_relation = True
                    break
            if not is_relation:
                delete_sql = "delete from {} where sid = '{}'".format(
                    table, sid)
                cursor.execute(delete_sql)
                conn.commit()
                print("delete sid = " + sid)
