from util.DBHelper import DBHelper
import pymysql


class DeWeight():
    def __init__(self, table):
        self.table = table
        # self.list = list
        db = DBHelper('fddx13')
        self.conn = db.getConnection()
        self.cur = self.conn.cursor()

    def merge(self, mrege_list):
        for l in mrege_list:
            #返回第一条
            return l

    def mergeList(self, mrege_list):
        templist = []
        gid = mrege_list[0]
        #print id
        for l in mrege_list:
            sql_one = "select * from {} WHERE id={}".format(self.table, l)
            self.cur.execute(sql_one)
            results = self.cur.fetchall()
            templist.append(results)
            update_sql = "update {} set tag1={} WHERE id={}".format(
                self.table, gid, l)
            # print(update_sql)
            # self.cur.execute(update_sql)
        #此方法会返回一条记录的列表
        #return self.merge(templist)
        return templist

    def is_in_table(self, table, field, field_value):
        search_sql_pre = "select count(*) as count from {} where `{}`='{}'"
        search_sql = search_sql_pre.format(table, field, field_value)
        self.cur.execute(search_sql)
        count = self.cur.fetchone()['count']
        if count < 1:
            return True
        else:
            return False

    def de_weight(self, merge_list, merge_table):
        # 当一组中存在来源为fdu时
        temp_tag = False
        for one in merge_list:
            data = one[0]
            if data['from'] == 'fdu':
                temp_tag = True
                print(data['from'])
                if self.is_in_table(merge_table, 'sid', data['sid']):
                    # del data['id']
                    insert_sql = 'insert into {} ({}) values ({}) '.format(
                        merge_table, ','.join(
                            "`{}`".format(i) for i in data.keys()), ','.join(
                                "'{}'".format(pymysql.escape_string(i))
                                for i in data.values()))
                    self.cur.execute(insert_sql)
                    self.conn.commit()
        if not temp_tag:
            # return one
            for one in merge_list:
                # 当不存在 fdu的时候返回第一个
                data = one[0]
                if self.is_in_table(merge_table, 'sid', data['sid']):
                    # del data['id']
                    insert_sql = 'insert into {} ({}) values ({}) '.format(
                        merge_table, ','.join(
                            "`{}`".format(i) for i in data.keys()), ','.join(
                                "'{}'".format(pymysql.escape_string(i))
                                for i in data.values()))
                    self.cur.execute(insert_sql)
                    self.conn.commit()
                return data
                # return one

    def de_weight_isbn2(self, merge_list, merge_table):
        # 当一组中存在来源为fdu时
        # print(merge_list)
        if len(merge_list) == 2 and (merge_list[0][0]['from'] != merge_list[1][0]['from']):
            print(merge_list[0][0]['from'],merge_list[1][0]['from'])
            for one in merge_list:
                data = one[0]
                if data['from'] == 'fdu':
                    print(data['from'])
                    if self.is_in_table(merge_table, 'sid', data['sid']):
                        # del data['id']
                        insert_sql = 'insert into {} ({}) values ({}) '.format(
                            merge_table, ','.join(
                                "`{}`".format(i) for i in data.keys()), ','.join(
                                    "'{}'".format(pymysql.escape_string(i))
                                    for i in data.values()))
                        self.cur.execute(insert_sql)
                        self.conn.commit()
        else:
            for one in merge_list:
                data = one[0]
                if self.is_in_table(merge_table, 'sid', data['sid']):
                        # del data['id']
                        insert_sql = 'insert into {} ({}) values ({}) '.format(
                            merge_table, ','.join(
                                "`{}`".format(i) for i in data.keys()), ','.join(
                                    "'{}'".format(pymysql.escape_string(i))
                                    for i in data.values()))
                        self.cur.execute(insert_sql)
                        self.conn.commit()
                    

        
    def many(self, filter_list, merge_table, dan_table, merged_table):
        double_list = []
        sql = "select {} from {}".format(','.join(filter_list), self.table)
        self.cur.execute(sql)
        results_fields = self.cur.fetchall()
        print(len(results_fields))
        # news_ids=[]
        # for field in results_fields:
        #     t=true
        #     for field2 in results_fields:
        #         for key in  field.keys():
        #             t=true
        #             if field[key]==field2[key]:
        #                 t=False

        # exit()
        # print(len(news_ids))
        # exit()
        # results_fields=list(set(results_fields))

        for r in results_fields:
            # print r
            if 1 == 1:
                where = ' and '.join(
                    "{}='{}'".format(k, v) for k, v in r.items())
                sqlwhere = "select id from {} WHERE {}".format(
                    self.table, where)
                # print(sqlwhere)
                self.cur.execute(sqlwhere)
                results_counts = self.cur.fetchall()
                if (len(results_counts) > 1):
                    templist = []
                    for item in results_counts:
                        templist.append(item['id'])
                    print(templist)
                    one = self.mergeList(templist)

                    for o in one:
                        # print(o)

                        data = o[0]
                        double_list.append(data['sid'])
                        search_sql = "select count(*) as count from {} where sid='{}'".format(
                            merge_table, data['sid'])
                        self.cur.execute(search_sql)
                        count = self.cur.fetchone()['count']

                        # print(self.cur.fetchone()['count'])
                        del data['id']
                        if count < 1:
                            insert_sql = 'insert into {} ({}) values ({}) '.format(
                                merge_table, ','.join(
                                    "`{}`".format(i) for i in data.keys()),
                                ','.join(
                                    "'{}'".format(pymysql.escape_string(i))
                                    for i in data.values()))

                            self.cur.execute(insert_sql)
                            self.conn.commit()
                    self.de_weight_isbn2(one, merged_table)
                    # print(insert_sql)
        double_list = list(set(double_list))
        dan_sql = "insert into {} (sid,title_cn,title_py,title_foreign,decription,book_number,binding,price,isbn,category,series,attachment,size,publish_co,pages,publish_address,publish_year,start_year ,end_year,`type`,version,`language`,z200,v200,i200,h200,g200,f200,e200,d200,c200,`from`) select sid,title_cn,title_py,title_foreign,decription,book_number,binding,price,isbn,category,series,attachment,size,publish_co,pages,publish_address,publish_year,start_year ,end_year,`type`,version,`language`,z200,v200,i200,h200,g200,f200,e200,d200,c200,`from` from {} where sid not in (select sid from {})".format(
            dan_table, self.table, merge_table)
        self.cur.execute(dan_sql)
        self.conn.commit()
        print(len(double_list))

        # 将merged表插入单表
        merge_dan_sql = "insert into `{}` (sid,title_cn,title_py,title_foreign,decription,book_number,binding,price,isbn,category,series,attachment,size,publish_co,pages,publish_address,publish_year,start_year ,end_year,`type`,version,`language`,z200,v200,i200,h200,g200,f200,e200,d200,c200,`from`)  select sid,title_cn,title_py,title_foreign,decription,book_number,binding,price,isbn,category,series,attachment,size,publish_co,pages,publish_address,publish_year,start_year ,end_year,`type`,version,`language`,z200,v200,i200,h200,g200,f200,e200,d200,c200,`from` from `{}`".format(
            dan_table, merged_table)
        print(merge_dan_sql)
        self.cur.execute(merge_dan_sql)
        self.conn.commit()

        #     else:
        #         where= ' and '.join("{}='{}'".format(i,MySQLdb.escape_string(r[k])) for k,i in enumerate(list))
        #         sqlwhere = "select id as count from {} WHERE {}".format(tableName,where)
        #         #print sqlwhere
        #         cur.execute(sqlwhere)
        #         results_counts = cur.fetchall()
        #         if (len(results_counts) > 0):
        #             templist = []
        #             for count in results_counts:
        #                 templist.append(count[0])
        #             mergeList(templist)

    def many2(self, filter_list, merge_table, dan_table, merged_table):
        double_list = []
        sql = "select {} from {}".format(','.join(filter_list), self.table)
        self.cur.execute(sql)
        results_fields = self.cur.fetchall()
        print(len(results_fields))
        for r in results_fields:
            # print r
            if 1 == 1:
                where = ' and '.join(
                    "{}='{}'".format(k, pymysql.escape_string(v) if v else '') for k, v in r.items())
                sqlwhere = "select id from {} WHERE {}".format(
                    self.table, where)
                # print(sqlwhere)
                self.cur.execute(sqlwhere)
                results_counts = self.cur.fetchall()
                if (len(results_counts) > 1):
                    templist = []
                    for item in results_counts:
                        templist.append(item['id'])
                    print(templist)
                    one = self.mergeList(templist)

                    for o in one:
                        # print(o)

                        data = o[0]
                        double_list.append(data['sid'])
                        # where = ' and '.join("{}='{}'".format(k, pymysql.escape_string(data[k]) if data[k] else '') for k in filter_list)
                        search_sql = "select count(*) as count from {} where id = '{}'".format(
                            merge_table, data['id'])
                        print(search_sql)
                        self.cur.execute(search_sql)
                        count = self.cur.fetchone()['count']

                        # print(self.cur.fetchone()['count'])
                        # del data['id']
                        if count < 1:
                            insert_sql = 'insert into {} ({}) values ({}) '.format(
                                merge_table, ','.join(
                                    "`{}`".format(i) for i in data.keys()),
                                ','.join(
                                    "'{}'".format(pymysql.escape_string(str(i)) if i else '')
                                    for i in data.values()))

                            self.cur.execute(insert_sql)
                            self.conn.commit()
        #             self.de_weight_isbn2(one, merged_table)
        #             # print(insert_sql)
        # double_list = list(set(double_list))
        # dan_sql = "insert into {} (sid,title_cn,title_py,title_foreign,decription,book_number,binding,price,isbn,category,series,attachment,size,publish_co,pages,publish_address,publish_year,start_year ,end_year,`type`,version,`language`,z200,v200,i200,h200,g200,f200,e200,d200,c200,`from`) select sid,title_cn,title_py,title_foreign,decription,book_number,binding,price,isbn,category,series,attachment,size,publish_co,pages,publish_address,publish_year,start_year ,end_year,`type`,version,`language`,z200,v200,i200,h200,g200,f200,e200,d200,c200,`from` from {} where sid not in (select sid from {})".format(
        #     dan_table, self.table, merge_table)
        # self.cur.execute(dan_sql)
        # self.conn.commit()
        # print(len(double_list))

        # # 将merged表插入单表
        # merge_dan_sql = "insert into `{}` (sid,title_cn,title_py,title_foreign,decription,book_number,binding,price,isbn,category,series,attachment,size,publish_co,pages,publish_address,publish_year,start_year ,end_year,`type`,version,`language`,z200,v200,i200,h200,g200,f200,e200,d200,c200,`from`)  select sid,title_cn,title_py,title_foreign,decription,book_number,binding,price,isbn,category,series,attachment,size,publish_co,pages,publish_address,publish_year,start_year ,end_year,`type`,version,`language`,z200,v200,i200,h200,g200,f200,e200,d200,c200,`from` from `{}`".format(
        #     dan_table, merged_table)
        # print(merge_dan_sql)
        # self.cur.execute(merge_dan_sql)
        # self.conn.commit()

        #     else:
        #         where= ' and '.join("{}='{}'".format(i,MySQLdb.escape_string(r[k])) for k,i in enumerate(list))
        #         sqlwhere = "select id as count from {} WHERE {}".format(tableName,where)
        #         #print sqlwhere
        #         cur.execute(sqlwhere)
        #         results_counts = cur.fetchall()
        #         if (len(results_counts) > 0):
        #             templist = []
        #             for count in results_counts:
        #                 templist.append(count[0])
        #             mergeList(templist)
