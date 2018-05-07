'''
parseMac module
'''

import re
from collections import defaultdict
import xlrd
import pymysql
# import sys
# sys.path.append(r"/Users/daivd/www/python/oppbook")
from util.TraSim.TraSim import Tra2Sim
from util.DBHelper import DBHelper
from entity.Items import *
'''    db数据库
    table 要插入的表
    source 来源 nlc fdu
    unique excel的唯一键的列
    field marc字段
    field_value marc字段值
'''


class parseMarc:
    def __init__(self, db, table, source, unique_index, field_index, field_value_index):
            self.table = table  
            self.source = source
            self.unique_index = unique_index
            self.field_index = field_index
            self.field_value_index = field_value_index

            db = DBHelper(db)
            self.conn = db.getConnection()
            self.cur = self.conn.cursor()

    def funcname(self, parameter_list):
        pass

    def parse_row_nlc(self, row):
            
        REGPX_A = re.compile(r'\|a\s?([^\|]+)')
        REGPX_B = re.compile(r'\|b\s?([^\|]+)')
        REGPX_C = re.compile(r'\|c\s?([^\|]+)')
        REGPX_D = re.compile(r'\|d\s?([^\|]+)')
        REGPX_E = re.compile(r'\|e\s?([^\|]+)')
        REGPX_F = re.compile(r'\|f\s?([^\|]+)')
        REGPX_G = re.compile(r'\|g\s?([^\|]+)')
        REGPX_H = re.compile(r'\|h\s?([^\|]+)')
        REGPX_I = re.compile(r'\|i\s?([^\|]+)')
        REGPX_V = re.compile(r'\|v\s?([^\|]+)')
        REGPX_Z = re.compile(r'\|z\s?([^\|]+)')
        REGPX_9 = re.compile(r'\|9\s?([^\|]+)')

        for index, field in enumerate(row):
            if (type(field) == float):
                field = str(int(field))
            field = field.replace(' ', '')
            if field == '2001' and index == 3:
                # print(row[4])
                self.item.title_cn =  REGPX_A.findall(row[4])[0] if REGPX_A.findall(row[4]) else ''
                self.item.type = REGPX_B.findall(row[4])[0] if REGPX_B.findall(row[4]) else ''
                self.item.c200 = REGPX_C.findall(row[4])[0] if REGPX_C.findall(row[4]) else ''
                self.item.d200 = REGPX_D.findall(row[4])[0] if REGPX_D.findall(row[4]) else ''
                self.item.e200 = REGPX_E.findall(row[4])[0] if REGPX_E.findall(row[4]) else ''
                self.item.f200 = REGPX_F.findall(row[4])[0] if REGPX_F.findall(row[4]) else ''
                self.item.g200 = REGPX_G.findall(row[4])[0] if REGPX_G.findall(row[4]) else ''
                self.item.h200 = REGPX_H.findall(row[4])[0] if REGPX_H.findall(row[4]) else ''
                self.item.i200 = REGPX_I.findall(row[4])[0] if REGPX_I.findall(row[4]) else ''
                self.item.v200 = REGPX_V.findall(row[4])[0] if REGPX_V.findall(row[4]) else ''
                self.item.z200 = REGPX_Z.findall(row[4])[0] if REGPX_Z.findall(row[4]) else ''
                self.item.title_py = REGPX_9.findall(row[4])[0] if REGPX_9.findall(row[4]) else '' 
            if field == '330':
                self.item.decription = REGPX_A.findall(row[4])[0] if REGPX_A.findall(row[4]) else ''
                print(row[4])
            if field == '010' and index == 3:
                self.item.isbn = REGPX_A.findall(row[4])[0].replace('-','') if REGPX_A.findall(row[4]) else ''
                self.item.binding = REGPX_B.findall(row[4])[0] if REGPX_B.findall(row[4]) else ''
                self.item.price = REGPX_D.findall(row[4])[0] if REGPX_D.findall(row[4]) else ''
            if field == '210' and index == 3:
                self.item.publish_co = REGPX_C.findall(row[4])[0] if REGPX_C.findall(row[4]) else ''
                self.item.publish_address = REGPX_A.findall(row[4])[0] if REGPX_A.findall(row[4]) else ''
                self.item.publish_year = REGPX_D.findall(row[4])[0] if REGPX_D.findall(row[4]) else ''
                # temp = re.findall(PUBDATE_STANDARD_REGPX,  self.item.publish_year)
                #     if temp:
                #         if len(temp) > 1:
                #                 if '-' in temp[0]:
                #                     item['irPubdate_standard_start'] = (temp[0])[0:len(temp[0]) - 1] + ((5 - len(temp[0])) * "0")
                #                     item['irPubdate_standard_end'] = temp[1] + ((4 - len(temp[1])) * "9")
                #                 elif '?-' in temp[0]:
                #                     item['irPubdate_standard_start'] = (temp[0])[0:len(temp[0]) - 2] + ((6 - len(temp[0])) * "9")
                #                     item['irPubdate_standard_end'] = temp[1]
                #                 else:
                #                     item['irPubdate_standard_start'] = temp[0] + ((4 - len(temp[0])) * "0")
                #                     item['irPubdate_standard_end'] = temp[1] + ((4 - len(temp[1])) * "9")
                #             else:
                #                 if '-?' in temp[0]:
                #                     base = (temp[0])[0:-2]
                #                     cha = 4 - len(base)
                #                     item['irPubdate_standard_start'] = base + (cha * "0")
                #                     item['irPubdate_standard_end'] = base + (cha * "9")
                #                 elif '-' in temp[0]:
                #                     base = (temp[0])[0:-1]
                #                     cha = 4 - len(base)
                #                     item['irPubdate_standard_start'] = base + (cha * "0")
                #                     item['irPubdate_standard_end'] = "2999"
                #                 else:
                #                     item['irPubdate_standard_start'] = temp[0] + ((4 - len(temp[0])) * "0")
                #                     item['irPubdate_standard_end'] = temp[0] + ((4 - len(temp[0])) * "0")
            if field == '1010' or field == '101':
                self.item.language = REGPX_A.findall(row[4])[0] if REGPX_A.findall(row[4]) else ''
            if field == '205':
                self.item.version = REGPX_A.findall(row[4])[0] if REGPX_A.findall(row[4]) else ''
            if field == '215':
                self.item.pages = REGPX_A.findall(row[4])[0] if REGPX_A.findall(row[4]) else ''
                self.item.size = REGPX_D.findall(row[4])[0] if REGPX_D.findall(row[4]) else ''
                self.item.attachment = REGPX_D.findall(row[4])[0] if REGPX_D.findall(row[4]) else ''
            if field == '225':
                self.item.series = REGPX_A.findall(row[4])[0] if REGPX_A.findall(row[4]) else ''
            if field == '690' or field == '686':
                self.item.category = REGPX_A.findall(row[4])[0] if REGPX_A.findall(row[4]) else ''
            #         # if '455' in field and index == 3:
            #         #     item['irMother'] =Tra2Sim(row[4])
            #         # item['irKeyNum'] = row[0]
            self.item.sid = row[0]
            self.item.source = 'nlc'

    def parse_row(self, row):

        REGPX_ISBN = re.compile(r'\d{9,12}[0-9a-zA-Z]')

        if self.source == 'nlc':
            REGPX_A = re.compile(r'\|a\s?([^\|]+)')
            REGPX_B = re.compile(r'\|b\s?([^\|]+)')
            REGPX_C = re.compile(r'\|c\s?([^\|]+)')
            REGPX_D = re.compile(r'\|d\s?([^\|]+)')
            REGPX_E = re.compile(r'\|e\s?([^\|]+)')
            REGPX_F = re.compile(r'\|f\s?([^\|]+)')
            REGPX_G = re.compile(r'\|g\s?([^\|]+)')
            REGPX_H = re.compile(r'\|h\s?([^\|]+)')
            REGPX_I = re.compile(r'\|i\s?([^\|]+)')
            REGPX_V = re.compile(r'\|v\s?([^\|]+)')
            REGPX_Z = re.compile(r'\|z\s?([^\|]+)')
            REGPX_9 = re.compile(r'\|9\s?([^\|]+)')
            REGPX_ALL = re.compile(r'\|[a-z0-9]\s?([^\|]+)')
            PUBDATE_STANDARD_REGPX = re.compile(r'([0-9]{3,4}\-?\??)')

            self.item.source = 'nlc'
        else: 
            REGPX_A = re.compile(r'\$\$a\s?([^\$]+)')
            REGPX_B = re.compile(r'\$\$b\s?([^\$]+)')
            REGPX_C = re.compile(r'\$\$c\s?([^\$]+)')
            REGPX_D = re.compile(r'\$\$d\s?([^\$]+)')
            REGPX_E = re.compile(r'\$\$e\s?([^\$]+)')
            REGPX_F = re.compile(r'\$\$f\s?([^\$]+)')
            REGPX_G = re.compile(r'\$\$g\s?([^\$]+)')
            REGPX_H = re.compile(r'\$\$h\s?([^\$]+)')
            REGPX_I = re.compile(r'\$\$i\s?([^\$]+)')
            REGPX_V = re.compile(r'\$\$v\s?([^\$]+)')
            REGPX_Z = re.compile(r'\$\$z\s?([^\$]+)')
            REGPX_9 = re.compile(r'\$\$9\s?([^\$]+)')
            REGPX_ALL = re.compile(r'\$\$[a-z0-9]\s?([^\$]+)')
            PUBDATE_STANDARD_REGPX = re.compile(r'([0-9]{3,4}[\-\～]?\??)')
            self.item.source = 'fdu'

        field = row[self.field_index]
        value = row[self.field_value_index]
        if (type(field) == float):
            field = str(int(field))
        field = field.replace(' ', '')
        if field == '2001':
            REGPX_A_VALUE = REGPX_A.findall(value)
            REGPX_C_VALUE =  REGPX_C.findall(value)
            REGPX_D_VALUE =  REGPX_D.findall(value)
            REGPX_E_VALUE =  REGPX_E.findall(value)
            REGPX_F_VALUE =  REGPX_F.findall(value)
            REGPX_G_VALUE =  REGPX_G.findall(value)
            REGPX_H_VALUE =  REGPX_H.findall(value)
            REGPX_I_VALUE =  REGPX_I.findall(value)
            REGPX_V_VALUE =  REGPX_V.findall(value)
            REGPX_Z_VALUE =  REGPX_Z.findall(value)
            REGPX_9_VALUE =  REGPX_9.findall(value)

            if REGPX_A_VALUE:
                for v in REGPX_A_VALUE:
                    self.item.title_cn += (v.strip(' ')+'@@@')
            self.item.type = REGPX_B.findall(value)[0] if REGPX_B.findall(value) else ''
            if REGPX_C_VALUE:
                for v in REGPX_C_VALUE:
                    self.item.c200 += (v.strip(' ')+'@@@')
            if REGPX_D_VALUE:
                for v in REGPX_D_VALUE:
                    self.item.d200 += (v.strip(' ')+'@@@')
            if REGPX_E_VALUE:
                for v in REGPX_E_VALUE:
                    self.item.e200 += (v.strip(' ')+'@@@')
            if REGPX_F_VALUE:
                for v in REGPX_F_VALUE:
                    self.item.f200 += (v.strip(' ')+'@@@')
            if REGPX_G_VALUE:
                for v in REGPX_G_VALUE:
                    self.item.g200 += (v.strip(' ')+'@@@')
            if REGPX_H_VALUE:
                for v in REGPX_H_VALUE:
                    self.item.h200 += (v.strip(' ')+'@@@')
            if REGPX_I_VALUE:
                for v in REGPX_I_VALUE:
                    self.item.i200 += (v.strip(' ')+'@@@')
            if REGPX_V_VALUE:
                for v in REGPX_V_VALUE:
                    self.item.v200 += (v.strip(' ')+'@@@')
            if REGPX_Z_VALUE:
                for v in REGPX_Z_VALUE:
                    self.item.z200 += (v.strip(' ')+'@@@')


            # self.item.title_cn =  REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
            # self.item.type = REGPX_B.findall(value)[0] if REGPX_B.findall(value) else ''
            # self.item.c200 = REGPX_C.findall(value)[0] if REGPX_C.findall(value) else ''
            # self.item.d200 = REGPX_D.findall(value)[0] if REGPX_D.findall(value) else ''
            # self.item.e200 = REGPX_E.findall(value)[0] if REGPX_E.findall(value) else ''
            # self.item.f200 = REGPX_F.findall(value)[0] if REGPX_F.findall(value) else ''
            # self.item.g200 = REGPX_G.findall(value)[0] if REGPX_G.findall(value) else ''
            # self.item.h200 = REGPX_H.findall(value)[0] if REGPX_H.findall(value) else ''
            # self.item.i200 = REGPX_I.findall(value)[0] if REGPX_I.findall(value) else ''
            # self.item.v200 = REGPX_V.findall(value)[0] if REGPX_V.findall(value) else ''
            # self.item.z200 = REGPX_Z.findall(value)[0] if REGPX_Z.findall(value) else ''
            # self.item.title_py = REGPX_9.findall(value)[0] if REGPX_9.findall(value) else ''
        if self.source == 'fdu':
            if field == '001':
                self.item.fdu_sys_no = value
        if field[0] == '6' and (field[2] == '0' or field[2]=='1'):
            temp_6xx = REGPX_ALL.findall(value)
            if temp_6xx:
                for one in temp_6xx:
                    self.item.subject_plus += (one+'@@@')  
           
        if field == '330':
            self.item.description = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
            print(row[self.field_value_index])
        if field[0] == '3':
            temp_3xx = REGPX_ALL.findall(value)
            if temp_3xx:
                for one in temp_3xx:
                    self.item.description_plus += (one+'@@@')
        if field == '010' or field == '091':
            isbn = REGPX_A.findall(value)[0].replace('-','') if REGPX_A.findall(value) else ''
            if REGPX_ISBN.findall(isbn):
                self.item.isbn += (isbn+'@@@')
            else:
                self.item.book_number = isbn
            self.item.binding = REGPX_B.findall(value)[0] if REGPX_B.findall(value) else ''
            self.item.price = REGPX_D.findall(value)[0] if REGPX_D.findall(value) else ''
        if field == '210':
            self.item.publish_co = REGPX_C.findall(value)[0] if REGPX_C.findall(value) else ''
            self.item.publish_address = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
            self.item.publish_year = REGPX_D.findall(value)[0] if REGPX_D.findall(value) else ''
            temp = re.findall(PUBDATE_STANDARD_REGPX,  self.item.publish_year)
            if temp:
                if len(temp) > 1:
                    if '-' in temp[0]:
                        self.item.start_year = (temp[0])[0:len(temp[0]) - 1] + ((5 - len(temp[0])) * "0")
                        self.item.end_year = temp[1] + ((4 - len(temp[1])) * "9")
                    elif '?-' in temp[0]:
                        self.item.start_year = (temp[0])[0:len(temp[0]) - 2] + ((6 - len(temp[0])) * "9")
                        self.item.end_year = temp[1]
                    else:
                        self.item.start_year = temp[0] + ((4 - len(temp[0])) * "0")
                        self.item.end_year = temp[1] + ((4 - len(temp[1])) * "9")
                else:
                    if '-?' in temp[0]:
                        base = (temp[0])[0:-2]
                        cha = 4 - len(base)
                        self.item.start_year = base + (cha * "0")
                        self.item.end_year = base + (cha * "9")
                    elif '-' in temp[0] or '～' in temp[0]:
                        base = (temp[0])[0:-1]
                        cha = 4 - len(base)
                        self.item.start_year = base + (cha * "0")
                        self.item.end_year = "2999"
                    else:
                        self.item.start_year = temp[0] + ((4 - len(temp[0])) * "0")
                        self.item.end_year = temp[0] + ((4 - len(temp[0])) * "0")
                       
        if field == '1010' or field == '101':
            self.item.language = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if field == '205':
            self.item.version = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if field == '215':
            self.item.pages = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
            self.item.size = REGPX_D.findall(value)[0] if REGPX_D.findall(value) else ''
            self.item.attachment = REGPX_D.findall(value)[0] if REGPX_D.findall(value) else ''
        if field == '225':
            self.item.series = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if field == '690' or field == '686':
            self.item.category = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
            #         # if '455' in field and index == 3:
            #         #     item['irMother'] =Tra2Sim(value)
            #         # item['irKeyNum'] = row[0]
        self.item.sid = row[self.unique_index]
        

            

    def parse_item(self, v):     
        self.item = Items()   
        for row in v:
            self.parse_row(row)
        item_dict = self.item.__dict__
        return item_dict

    # 获得文件中以唯一键为key 所有行组成的列表为值得字典
    def get_file_dict(self, file_path):
        book_dic = defaultdict(list)  # 以id为键名各行数据为键值的字典
        data = xlrd.open_workbook(file_path)
        sheet = data.sheets()[0]  # 通过索引顺序获取第一个工作表
        nrows = sheet.nrows  # 行数
        print(nrows)
        unique_index = self.unique_index
        for i in range(1, nrows):
            row = sheet.row_values(i)
            book_dic[row[unique_index]].append(row)
        return book_dic

    def parse_marc(self, file_path):
        all_data_insert = []  # 最终的入库记录
        book_dic = self.get_file_dict(file_path)

        for k, v in book_dic.items():
            item_dict = self.parse_item(v)
            all_data_insert.append(item_dict)
            # print(item_dict)
        for one_record in all_data_insert:
            if 'isbn' in one_record.keys():
                one_record['isbn'] = one_record['isbn'].strip('@@@')
            if 'description_plus' in one_record.keys():
                one_record['description_plus'] = one_record['description_plus'].strip('@@@')
            sql = 'insert into {} ({}) values ({}) '.format(self.table, ','.join(one_record.keys()),','.join('%({})s'.format(i) for i in one_record.keys()))
            self.cur.executemany(sql, (one_record,))
            self.conn.commit()

        self.cur.close()
        self.conn.close()

    def update_has_table(self, file_path):
        book_dic = self.get_file_dict(file_path)
        # 获得要更新的表中的所有记录
        sql = "select * from {}".format(self.table)
        self.cur.execute(sql)
        items = self.cur.fetchall()
        update_sql_pre = "update {} {} where id = '{}'"
        for item in items:
            for k, v in book_dic.items():
                if item['sid'] == k:
                    item_dict = self.parse_item(v)
                    u_str = 'set '
                    for key in item_dict.keys():
                        f_v = item_dict[key].strip('@@@')
                        f_v = pymysql.escape_string(f_v)
                        u_str += ("`"+key+"`" + '=' + "'" + f_v + "'" + ',')
                        update_sql = update_sql_pre.format(self.table, u_str.strip(","),item['id'])
                        self.cur.execute(update_sql)
                        self.conn.commit()
        self.cur.close()
        self.conn.close()

            

if __name__ == '__main__':
    parse_marc = parseMarc()
    parse_marc.parse_cn_marc('/Users/daivd/www/python/data/nlc_president.xlsx')
