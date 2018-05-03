# import sys
# sys.path.append(r"/Users/daivd/www/python/oppbook")
from util.TraSim.langconv import *


def Tra2Sim(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence


def Sim2Tra(sentence):
    '''
    将sentence中的简体字转为繁体字
    :param sentence: 待转换的句子
    :return: 将句子中简体字转换为繁体字之后的句子
    '''
    sentence = Converter('zh-hant').convert(sentence)
    return sentence


if __name__ == "__main__":
    traditional_sentence = '憂郁的臺灣烏龜'
    simplified_sentence = Tra2Sim(traditional_sentence)
    print(simplified_sentence)