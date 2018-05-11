from dao.parseMarc import *
from dao.Uncorrelated import *
from dao.TransformChinese import *
from dao.UpdateField import *
from dao.DeWeight import *
from dao.Designate import *


# parse = parseMarc('fddx12','books_nlc_e_m', 'nlc', 0, 3, 4)
# parse.parse_marc('/Users/daivd/www/python/data/nlc_engineering_medicine.xlsx')

# parse = parseMarc('fddx12','books_fdu', 'fdu', 2, 3, 5)
# parse.parse_marc('/Users/daivd/www/python/data/fdu_president.xlsx')

# parse = parseMarc('fddx12', 'books_qk_temp', 'fdu', 1, 2, 4)
# parse.parse_marc('/Users/daivd/www/python/data/add/books_qk_back.xlsx')

# parse = parseMarc('fddx12', 'books_book_temp', 'fdu', 1, 2, 4)
# parse.parse_marc('/Users/daivd/www/python/data/add/books_book_dan_dan20180503.xlsx')

# parse = parseMarc('fddx11', 'books_book_dan_dan_dan2', 'fdu', 2, 3, 5)
# parse.parse_marc('/Users/daivd/www/python/data/p_marc/fdu_president.xlsx')

# parse = parseMarc('fddx11', 'books_book_dan_dan_dan2', 'nlc', 0, 3, 4)
# parse.parse_marc('/Users/daivd/www/python/data/p_marc/nlc_president.xlsx')
# parse = parseMarc('fddx', 'books_president', 'fdu', 2, 3, 5)
# parse.parse_marc('/Users/sower/www/python3/parsebook/data/excel/fdu_president.xlsx')

# parse = parseMarc('fddx', 'books_president', 'nlc', 0, 3, 4)
# parse.parse_marc('/Users/sower/www/python3/parsebook/data/excel/nlc_president.xlsx')

# trans = TransformChinese(db='fddx', table='books_president')
# keys = ('title_cn', 'description', 'description_plus', 'binding', 'series', 'publish_co', 'pages',
#         'publish_address', 'type', 'g200', 'f200', 'e200', 'version',
#         'publish_year')
# keys2 = ('author', 'duty')
# trans.go((keys))

# parse = parseMarc('fddx10', 'books', 'fdu', 2, 3, 5)
# parse.parse_marc('/Users/daivd/www/python/data/fdu_professor.xlsx')

# parse = parseMarc('fddx10', 'books', 'nlc', 0, 3, 4)
# parse.parse_marc('/Users/daivd/www/python/data/nlc_engineering_medicine.xlsx')

# parse = parseMarc('fddx11', 'books_book_dan_dan_dan', 'nlc', 0, 1, 2)
# parse.update_has_table('/Users/daivd/www/python/data/add/nlc_zzr.xlsx')

# parse = parseMarc('fddx13', 'xwlw4', 'fdu', 1, 2, 4)

# for i in range(1, 8):   

#     print("/Users/daivd/www/python/data/xw_excel/xw{}.xlsx".format(i))
#     parse.parse_xw("/Users/daivd/www/python/data/xw_excel/xw{}.xlsx".format(i))

# parse.update_table_field_by_self('xwlw_final3','complete_time','year')
# parse.update_table_by_table("xwlw4","xwlw3","student_no",['title_cn','title_foreign','type','category','language','discipline_no',
# 'discipline_name','student_type','degree','secrecy_level','author','school','department','profession','first_tutor_school',
# 'first_tutor_department','first_tutor_profession','second_tutor_name','second_tutor_school','second_tutor_department','second_tutor_profession',
# 'complete_time','oral_time','keyword_cn','keyword_foreign','brief_cn','brief_foreign','total_pages',
# 'reference','reference_count','subsidize','open_time','property_no','collection_no','calis_oid','formate','create_date',
# 'doc_id','full_text','carrier','collection_location','sbm'])

# parse = parseMarc('fddx12','books_ztbm_temp', 'nlc', 0, 3, 4)
# parse.parse_marc('/Users/daivd/www/python/data/add/nlc_ztbm.xlsx')

# trans = TransformChinese(db='fddx11', table='books_book_dan_dan_dan2')
# keys = ('title_cn', 'description', 'description_plus', 'binding', 'series', 'publish_co', 'pages',
#         'publish_address', 'type', 'g200', 'f200', 'e200', 'version',
#         'publish_year','subject_plus')
# keys2 = ('author', 'duty')
# trans.go((keys))

# from dao.DeWeight import *    
# deWeight = DeWeight('books_lw')
# deWeight.many(['title_cn','f200'],'books_lw_shuan','books_lw_dan','books_lw_shuan_m')

# deWeight = DeWeight('books_gj')
# deWeight.many(['title_cn','isbn','pages','start_year','publish_co'],'books_gj_shuan','books_gj_dan','books_gj_shuan_m')

# deWeight = DeWeight('books_book')
# deWeight.many(['title_cn','isbn','pages','start_year','publish_co'],'books_book_shuan','books_book_dan','books_book_shuan_m')
# deWeight = DeWeight('books_book_dan')
# deWeight.many(['isbn','title_cn'],'books_book_shuan','books_book_dan_dan','books_book_shuan_m')

deWeight = DeWeight('xwlw7')
deWeight.many2(['title_cn','author'],'xwlw_final3_shuan2','xwlw_final3_dan','xwlw_final3_shuan_m')


# uncorrelated = Uncorrelated('fddx10')
# uncorrelated.go('nlc_e_m_base', 'duty', 'scholar')

# 更新指定字段
# update_field = UpdateField(db='fddx10', table='fdu_p_base')
# update_field.update_type_cluster('fdu')

# designate = Designate('fddx11')
# designate.designate_by_scholar('scholar_president', 'duty2', 'books_book_dan_dan_dan2',
#                                'duty_book3')

# parse = parseMarc('fddx13','xwlw3', 'fdu', 0, 3, 4)
# parse.parse_txt('/Users/daivd/www/python/data/xw.txt')        

# designate = Designate('fddx10')
# designate.take_master_book('master','duty','books','target_table')

# uncorrelated = Uncorrelated('fddx10')
# uncorrelated.go('target_table', 'duty', 'master')

# parse = parseMarc('fddx13', 'xwlw7', 'fdu', 1, 2, 4)

# parse.update_table_by_table2("xwlw_final3","xw001","sid",['fdu_sys_no'])

# for i in range(1, 8):
#     print("/Users/daivd/www/python/data/xw_excel/xw{}.xlsx".format(i))
#     parse.parse_xw("/Users/daivd/www/python/data/xw_excel/xw{}.xlsx".format(i))

# parse = parseMarc('fddx13','xwlw_txt', 'fdu', 0, 3, 4)
# parse.parse_txt('/Users/daivd/www/python/data/xw.txt') 
# 
# 
# parse.update_table_field_by_self('xwlw_final3','complete_time','year')
# parse.update_table_by_table2("xwlw7","xwlw_txt","student_no",['title_cn','title_foreign','type','category','language','discipline_no',
# 'discipline_name','student_type','degree','secrecy_level','author','school','department','profession','first_tutor_school',
# 'first_tutor_department','first_tutor_profession','second_tutor_name','second_tutor_school','second_tutor_department','second_tutor_profession',
# 'complete_time','oral_time','keyword_cn','keyword_foreign','brief_cn','brief_foreign','total_pages',
# 'reference','reference_count','subsidize','open_time','property_no','collection_no','calis_oid','formate','create_date',
# 'doc_id','full_text','carrier','collection_location','sbm'])    