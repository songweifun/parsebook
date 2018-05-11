'''
parseMac module
'''

import re
import os
from collections import defaultdict
import xlrd
import pymysql
# import sys
# sys.path.append(r"/Users/daivd/www/python/oppbook")
from util.TraSim.TraSim import Tra2Sim
from util.DBHelper import DBHelper
from entity.Items import *
from entity.Dissertation import *
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

    def parse_row_xw(self, row):

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
            if REGPX_D_VALUE:
                for v in REGPX_D_VALUE:
                    self.item.title_foreign += (v.strip(' ')+'@@@')

        if self.source == 'fdu':
            if field == '001':
                self.item.fdu_sys_no = value
        if field == '1010' or field == '101':
            self.item.language = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if field == '328':
            tempvalue = (REGPX_A.findall(value)[0]).replace("：",':').split(":") if REGPX_A.findall(value) else ''
            if tempvalue:
                print(tempvalue)
                if len(tempvalue) >1:
                    self.item.degree = tempvalue[1].strip(' ')
                self.item.profession = tempvalue[0].strip(' ')
        if field == '010' or field == '014':
            self.item.student_no = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if '701' in field:
            self.item.author = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if '702' in field:
            self.item.first_tutor_name = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
            self.item.second_tutor_name = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if field == '210':
            self.item.complete_time = REGPX_D.findall(value)[0] if REGPX_D.findall(value) else ''
            self.item.oral_time = REGPX_D.findall(value)[0] if REGPX_D.findall(value) else ''
            self.item.open_time = REGPX_D.findall(value)[0] if REGPX_D.findall(value) else ''
        if field == '610':
            self.item.keyword_cn = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if field == '215':
            self.item.total_pages = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if field == '690':
            self.item.category = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if field == '905':
            self.item.collection_no = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if field == '100':
            self.item.create_date = (REGPX_A.findall(value)[0])[0:8] if REGPX_A.findall(value) else ''
        if field == '205':
            self.item.carrier = REGPX_A.findall(value)[0] if REGPX_A.findall(value) else ''
        if field == '905':
            self.item.collection_location = REGPX_I.findall(value)[0] if REGPX_I.findall(value) else ''
        if field == 'SID':
            self.item.sbm = value
        self.item.sid = row[self.unique_index]
        

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
            for key in one_record.keys():
                one_record[key] = one_record[key].strip('@@@')
            # if 'isbn' in one_record.keys():
            #     one_record['isbn'] = one_record['isbn'].strip('@@@')
            # if 'description_plus' in one_record.keys():
            #     one_record['description_plus'] = one_record['description_plus'].strip('@@@')
            # if 'title_cn' in one_record.keys():
            #     one_record['title_cn'] = one_record['title_cn'].strip('@@@')
            # if 'c200' in one_record.keys():
            #     one_record['c200'] = one_record['c200'].strip('@@@')
            # if 'd200' in one_record.keys():
            #     one_record['d200'] = one_record['d200'].strip('@@@')
            sql = 'insert into {} ({}) values ({}) '.format(self.table, ','.join(one_record.keys()),','.join('%({})s'.format(i) for i in one_record.keys()))
            self.cur.executemany(sql, (one_record,))
        self.conn.commit()

        # self.cur.close()
        # self.conn.close()

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
    def parse_txt(self,file_path):
        if os.path.isfile(file_path):
            # import codecs
            # import chardet
            REGPX = re.compile(r'<REC>')
            REGPX_LANGUAGE=re.compile(r'<论文语种>:([.\s\S]+)\n')
            REGPX_DISCIPLINE_NO=re.compile(r'<学科代码>:([.\s\S]+)\n')
            REGPX_DISCIPLINE_NAME=re.compile(r'<学科名称>:([.\s\S]+)\n')
            REGPX_STUDENT_TYPE=re.compile(r'<学生类型>:([.\s\S]+)\n')
            REGPX_DEGREE=re.compile(r'<学位>:([.\s\S]+)\n')
            REGPX_SECRECY_LEVEL=re.compile(r'<保密级别>:([.\s\S]+)\n')
            REGPX_STUDENT_NO=re.compile(r'<学号>:([.\s\S]+)\n')
            REGPX_AUTHOR=re.compile(r'<作者>:([.\s\S]+)\n')
            REGPX_SCHOOL=re.compile(r'<学校>:([.\s\S]+)\n')
            REGPX_DEPARTMENT=re.compile(r'<院系>:([.\s\S]+)\n')
            REGPX_PROFESSION=re.compile(r'<专业>:([.\s\S]+)\n')

            REGPX_FIRST_TUTOR_NAME=re.compile(r'<第一导师姓名>:([.\s\S]+)\n')
            REGPX_FIRST_TUTOR_SCHOOL=re.compile(r'<第一导师学校>([.\s\S]+)\n')
            REGPX_FIRST_TUTOR_DEPARTMENT=re.compile(r'<第一导师院系>:([.\s\S]+)\n')
            REGPX_FIRST_TUTOR_PROFESSION=re.compile(r'<第一导师专业>:([.\s\S]+)\n')
            REGPX_SECOND_TUTOR_NAME=re.compile(r'<第二导师姓名>:([.\s\S]+)\n')
            REGPX_SECOND_TUTOR_SCHOOL=re.compile(r'<第二导师学校>([.\s\S]+)\n')
            REGPX_SECOND_TUTOR_DEPARTMENT=re.compile(r'<第二导师院系>:([.\s\S]+)\n')
            REGPX_SECOND_TUTOR_PROFESSION=re.compile(r'<第二导师专业>:([.\s\S]+)\n')


            REGPX_COMPLETE_TIME = re.compile(r'<论文完成日期>:([.\s\S]+)\n')
            REGPX_ORAL_TIME = re.compile(r'<论文答辩日期>:([.\s\S]+)\n')
            REGPX_TITLE_CN = re.compile(r'<论文题目\(中文\)>:([.\s\S]+)\n')
            REGPX_TITLE_FOREIGN = re.compile(r'<论文题目\(外文\)>:([.\s\S]+)\n')
            REGPX_COMPLETE_TIME = re.compile(r'<论文完成日期>:([.\s\S]+)\n')
            REGPX_ORAL_TIME = re.compile(r'<论文答辩日期>:([.\s\S]+)\n')
            # REGPX_TITLE_CN = re.compile(r'<论文题目(中文)>:([.\s\S]+)\n')
            # REGPX_TITLE_FOREIGN = re.compile(r'<论文题目(外文)>:([.\s\S]+)\n')


            REGPX_KEWORD_CN = re.compile(r'<论文关键字\(中文\)>:([.\s\S]+)[^<]')
            REGPX_KEYWORD_FOREIGN = re.compile(r'<论文关键字\(外文\)>:([.\s\S]+)[^<]')
            REGPX_BRIEF_CN = re.compile(r'<论文文摘\（中文\）>:([.\s\S]+)[^<]')
            REGPX_BRIEF_FOREIGN = re.compile(r'<论文文摘\（外文\）>:([.\s\S]+)[^<]')
            REGPX_TOTAL_PAGES = re.compile(r'<论文总页数>:([.\s\S]+)\n')
            REGPX_REFRENCE = re.compile(r'<论文参考文献>:([.\s\S]+)\n')

            REGPX_REFRENCE_COUNT = re.compile(r'<论文参考文献数>:([.\s\S]+)\n')
            REGPX_SUBSIDIZE = re.compile(r'<论文资助方>:([.\s\S]+)\n')
            REGPX_OPEN_TIME = re.compile(r'<论文开放日期>:([.\s\S]+)\n')
            REGPX_CATEGORY = re.compile(r'<中图分类号>:([.\s\S]+)\n')
            REGPX_PROPERTY_NO = re.compile(r'<财产号>:([.\s\S]+)\n')
            REGPX_COLLECTION_NO = re.compile(r'<馆藏号>:([.\s\S]+)\n')

            REGPX_CALIS_OID = re.compile(r'<Calis-OID>:([.\s\S]+)\n')
            REGPX_TYPE = re.compile(r'<资源类型>:([.\s\S]+)\n')
            REGPX_FORMATE = re.compile(r'<论文格式>:([.\s\S]+)\n')
            REGPX_CREATEDATE = re.compile(r'<CREATEDATE>([.\s\S]+)\n')
            REGPX_DOCID = re.compile(r'<DOCID>=([.\s\S]+)\n')
            REGPX_FULLTEXT = re.compile(r'<FULLText>=([.\s\S]+)[^<]')
            



            hander = open(file_path,'r',encoding="GB2312",errors='ignore')
            content = hander.readlines()
            hander.close()
            self.item = Dissertation()
            for line in content: 
                
                if REGPX.findall(line):
                    print(line)
                    print('______________')
                    item_dict = self.item.__dict__
                    # print(item_dict)
                    sql = 'insert into {} ({}) values ({}) '.format(self.table, ','.join(item_dict.keys()),','.join('%({})s'.format(i) for i in item_dict.keys()))
                    self.cur.executemany(sql, (item_dict,))
                    
                    self.item = Dissertation()
                if  REGPX_LANGUAGE.findall(line):
                    self.item.language = REGPX_LANGUAGE.findall(line)[0]
                if  REGPX_DISCIPLINE_NO.findall(line):
                    self.item.discipline_no = REGPX_DISCIPLINE_NO.findall(line)[0]
                if REGPX_DISCIPLINE_NAME.findall(line):
                    self.item.discipline_name = REGPX_DISCIPLINE_NAME.findall(line)[0] 
                if REGPX_STUDENT_TYPE.findall(line):
                    self.item.student_type = REGPX_STUDENT_TYPE.findall(line)[0] 
                if REGPX_DEGREE.findall(line):
                    self.item.degree = REGPX_DEGREE.findall(line)[0] 
                if REGPX_SECRECY_LEVEL.findall(line):
                    self.item.secrecy_level = REGPX_SECRECY_LEVEL.findall(line)[0] 
                if REGPX_STUDENT_NO.findall(line):
                    self.item.student_no = REGPX_STUDENT_NO.findall(line)[0] 
                if REGPX_AUTHOR.findall(line):
                    self.item.author= REGPX_AUTHOR.findall(line)[0] 
                if REGPX_SCHOOL.findall(line):
                    self.item.school = REGPX_SCHOOL.findall(line)[0] 
                if REGPX_DEPARTMENT.findall(line): 
                    self.item.department =REGPX_DEPARTMENT.findall(line)[0] 
                if REGPX_PROFESSION.findall(line):  
                    self.item.profession = REGPX_PROFESSION.findall(line)[0] 
                if REGPX_FIRST_TUTOR_NAME.findall(line):
                    self.item.first_tutor_name = REGPX_FIRST_TUTOR_NAME.findall(line)[0] 
                if REGPX_FIRST_TUTOR_SCHOOL.findall(line):
                    self.item.first_tutor_school = REGPX_FIRST_TUTOR_SCHOOL.findall(line)[0]
                if REGPX_FIRST_TUTOR_DEPARTMENT.findall(line):
                    self.item.first_tutor_department = REGPX_FIRST_TUTOR_DEPARTMENT.findall(line)[0] 
                if REGPX_FIRST_TUTOR_PROFESSION.findall(line):
                    self.item.first_tutor_profession = REGPX_FIRST_TUTOR_PROFESSION.findall(line)[0] 
                if REGPX_SECOND_TUTOR_NAME.findall(line):
                    self.item.second_tutor_name = REGPX_SECOND_TUTOR_NAME.findall(line)[0] 
                if REGPX_SECOND_TUTOR_SCHOOL.findall(line):
                    self.item.second_tutor_school = REGPX_SECOND_TUTOR_SCHOOL.findall(line)[0] 
                if REGPX_SECOND_TUTOR_DEPARTMENT.findall(line):
                    self.item.second_tutor_department = REGPX_SECOND_TUTOR_DEPARTMENT.findall(line)[0] 
                if REGPX_SECOND_TUTOR_PROFESSION.findall(line):
                    self.item.second_tutor_profession = REGPX_SECOND_TUTOR_PROFESSION.findall(line)[0] 
                if REGPX_COMPLETE_TIME.findall(line):
                    self.item.complete_time = REGPX_COMPLETE_TIME.findall(line)[0] 
                if REGPX_ORAL_TIME.findall(line):
                    self.item.oral_time = REGPX_ORAL_TIME.findall(line)[0]
                if REGPX_TITLE_CN.findall(line):
                    print(line)
                    self.item.title_cn = REGPX_TITLE_CN.findall(line)[0] 
                if REGPX_TITLE_FOREIGN.findall(line):
                    self.item.title_foreign= REGPX_TITLE_FOREIGN.findall(line)[0] 
                if REGPX_KEWORD_CN.findall(line):
                    self.item.keyword_cn = REGPX_KEWORD_CN.findall(line)[0]
                if REGPX_KEYWORD_FOREIGN.findall(line):
                    self.item.keyword_foreign =REGPX_KEYWORD_FOREIGN.findall(line)[0] 
                if REGPX_BRIEF_CN.findall(line):
                    self.item.brief_cn = REGPX_BRIEF_CN.findall(line)[0] 
                if REGPX_BRIEF_FOREIGN.findall(line):
                    self.item.brief_foreign = REGPX_BRIEF_FOREIGN.findall(line)[0] 
                if REGPX_TOTAL_PAGES.findall(line):
                    self.item.total_pages = REGPX_TOTAL_PAGES.findall(line)[0] 
                if REGPX_REFRENCE.findall(line):
                    self.item.reference = REGPX_REFRENCE.findall(line)[0]
                if REGPX_REFRENCE_COUNT.findall(line):
                    self.item.reference_count= REGPX_REFRENCE_COUNT.findall(line)[0] 
                if REGPX_SUBSIDIZE.findall(line):
                    self.item.subsidize = REGPX_SUBSIDIZE.findall(line)[0] 
                if REGPX_OPEN_TIME.findall(line):
                    self.item.open_time =REGPX_OPEN_TIME.findall(line)[0] 
                if REGPX_CATEGORY.findall(line):
                    self.item.category = REGPX_CATEGORY.findall(line)[0] 
                if REGPX_PROPERTY_NO.findall(line):
                    self.item.property_no= REGPX_PROPERTY_NO.findall(line)[0]
                if REGPX_COLLECTION_NO.findall(line):
                    self.item.collection_no = REGPX_COLLECTION_NO.findall(line)[0]
                if REGPX_CALIS_OID.findall(line):
                    self.item.calis_oid =REGPX_CALIS_OID.findall(line)[0] 
                if REGPX_TYPE.findall(line):
                    self.item.type = REGPX_TYPE.findall(line)[0]
                if REGPX_FORMATE.findall(line):
                    self.item.formate= REGPX_FORMATE.findall(line)[0] 
                if REGPX_CREATEDATE.findall(line):
                    self.item.create_date = REGPX_CREATEDATE.findall(line)[0]
                if REGPX_DOCID.findall(line):
                    self.item.doc_id =REGPX_DOCID.findall(line)[0] 
                if REGPX_FULLTEXT.findall(line):
                    self.item.full_text = REGPX_FULLTEXT.findall(line)[0]
                self.item.carrier = '打印本'
            self.conn.commit() 
            self.cur.close()
            self.conn.close()
            # print(chardet.detect(content))
            
    def parse_xw(self, file_path):
        book_dic = self.get_file_dict(file_path)
        for k, v in book_dic.items():
            self.item = Dissertation()
            for row in v:
                self.parse_row_xw(row)
            item_dict = self.item.__dict__
            # print(item_dict)
            for key in item_dict.keys():
                item_dict[key] = item_dict[key].strip('@@@')
            sql = 'insert into {} ({}) values ({}) '.format(self.table, ','.join(item_dict.keys()),','.join('%({})s'.format(i) for i in item_dict.keys()))
            self.cur.executemany(sql, (item_dict,))
        self.conn.commit()
        # self.cur.close()
        # self.conn.close()

    def update_has_table_xw(self, file_path,update_list):
        book_dic = self.get_file_dict(file_path)
        # 获得要更新的表中的所有记录
        sql = "select id,sid from {}".format(self.table)
        self.cur.execute(sql)
        items = self.cur.fetchall()
        update_sql_pre = "update {} {} where id = '{}'"
        for item in items:
            
            for k, v in book_dic.items():
                
                if item['sid'] == k:
                    u_str = "set sid ='{}',".format(item['sid'])
                    self.item = Dissertation()
                    for row in v:
                        self.parse_row_xw(row)
                    item_dict = self.item.__dict__
                    for key in update_list:
                        if key in item_dict.keys():
                            f_v = item_dict[key].strip('@@@') 
                            f_v = pymysql.escape_string(f_v) if f_v else ''
                            u_str += ("`"+key+"`" + '=' + "'" + f_v + "'" + ',')
                    update_sql = update_sql_pre.format(self.table, u_str.strip(","),item['id'])
                    print(update_sql)
                    self.cur.execute(update_sql)
                    self.conn.commit()
        # self.cur.close()
        # self.conn.close()

    def update_table_by_table(self,update_table,from_table,thekey,update_field_list):
        sql = "select {} from {}".format(thekey,update_table)
        self.cur.execute(sql)
        recs = self.cur.fetchall()
        for rec in recs:
            one_sql = "select {} from {} where {} = '{}'".format(','.join(update_field_list),from_table,thekey,rec[thekey])
            # print(one_sql)
            self.cur.execute(one_sql)
            one_detail = self.cur.fetchone()
            # print(one_detail)
            update_sql_pre = "update {} {} where {} = '{}'"
            u_str = 'set '
            if one_detail:
                for key in one_detail.keys():
                    f_v = one_detail[key]
                    f_v = pymysql.escape_string(f_v) if f_v else ''
                    u_str += ("`"+key+"`" + '=' + "'" + f_v + "'" + ',')
                    update_sql = update_sql_pre.format(update_table, u_str.strip(","),thekey,rec[thekey])
                    # print(update_sql)
                    self.cur.execute(update_sql)
        self.conn.commit()

    def update_table_by_table2(self,update_table,from_table,thekey,update_field_list):
        sql = "select {},{} from {}".format(thekey,','.join(update_field_list),from_table)
        self.cur.execute(sql)
        recs = self.cur.fetchall()
        update_sql_pre = "update {} {} where {} = '{}'"
       
        for rec in recs:
            u_str = 'set '
            for key in update_field_list:
                f_v = rec[key]
                f_v = pymysql.escape_string(f_v) if f_v else ''
                u_str += ("`"+key+"`" + '=' + "'" + f_v + "'" + ',')
            update_sql = update_sql_pre.format(update_table, u_str.strip(","),thekey,rec[thekey].strip('      '))
            print(rec[thekey])
            self.cur.execute(update_sql)
            self.conn.commit()

    def update_table_field_by_self(self,update_table,update_field_from,update_field_to):
        sql = "select id,{} from {}".format(update_field_from,update_table)
        self.cur.execute(sql)
        results = self.cur.fetchall()
        REGPX_YEAR = re.compile(r'\d{4}')
        for res in results:
            id = res['id']
            field = str(res[update_field_from])
            field_update_to = REGPX_YEAR.findall(field)[0] if REGPX_YEAR.findall(field) else ''
            print(field,field_update_to)

            update_field = "update {} set {} = '{}' where id ={}".format(update_table,update_field_to,field_update_to,id)
            self.cur.execute(update_field)
        self.conn.commit()
        self.cur.close()
        self.conn.close()
            

if __name__ == '__main__':
    parse_marc = parseMarc()
    parse_marc.parse_cn_marc('/Users/daivd/www/python/data/nlc_president.xlsx')
