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

# parse = parseMarc('fddx11', 'books_book_dan_dan_dan', 'fdu', 2, 3, 5)
# parse.update_has_table('/Users/daivd/www/python/data/fdu_president.xlsx')

# parse = parseMarc('fddx11', 'books_book_dan_dan_dan', 'nlc', 0, 3, 4)
# parse.update_has_table('/Users/daivd/www/python/data/nlc_president.xlsx')

# parse = parseMarc('fddx11', 'books_book_dan_dan_dan', 'nlc', 0, 1, 2)
# parse.update_has_table('/Users/daivd/www/python/data/add/nlc_zzr.xlsx')

# parse = parseMarc('fddx11', 'books_book_dan_dan_dan', 'fdu', 1, 2, 4)
# parse.update_has_table('/Users/daivd/www/python/data/add/nlc_zzr.xlsx')

trans = TransformChinese(db='fddx11', table='books_book_dan_dan_dan')
keys = ('title_cn', 'description', 'description_plus', 'binding', 'series', 'publish_co', 'pages',
        'publish_address', 'type', 'g200', 'f200', 'e200', 'version',
        'publish_year','subject_plus')
keys2 = ('author', 'duty')
trans.go((keys))

# from dao.DeWeight import *
# deWeight = DeWeight('books_lw')
# deWeight.many(['title_cn','f200'],'books_lw_shuan','books_lw_dan','books_lw_shuan_m')

# deWeight = DeWeight('books_gj')
# deWeight.many(['title_cn','isbn','pages','start_year','publish_co'],'books_gj_shuan','books_gj_dan','books_gj_shuan_m')

# deWeight = DeWeight('books_book')
# deWeight.many(['title_cn','isbn','pages','start_year','publish_co'],'books_book_shuan','books_book_dan','books_book_shuan_m')
# deWeight = DeWeight('books_book_dan')
# deWeight.many(['isbn','title_cn'],'books_book_shuan','books_book_dan_dan','books_book_shuan_m')


# uncorrelated = Uncorrelated('fddx10')
# uncorrelated.go('nlc_e_m_base', 'duty', 'scholar')

# 更新指定字段
# update_field = UpdateField(db='fddx10', table='fdu_p_base')
# update_field.update_type_cluster('fdu')

# designate = Designate('fddx11')
# designate.designate_by_scholar('scholar_president', 'duty', 'books_book_dan_dan_dan',
#                                'duty_book')
