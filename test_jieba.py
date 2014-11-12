#encoding=utf-8

import jieba
import chinese_dictionary
import bopomofo



def get_words(phrase):
    return jieba.cut(phrase)
    
def get_words_definitions(phrase):
    seg_list = jieba.cut(phrase)
    definition_list = []
    for word in seg_list:
        entry = ""
        for definition in chinese_dictionary.chinese_dictionary.get(word.encode("UTF-8"), "x"):
            entry= entry + "  " + str(definition) 
        definition

def get_bopomofo(word):
    for definition in chinese_dictionary.chinese_dictionary.get(word.encode("UTF-8"), "x"):
            print  bopomofo.pinyin_to_bopomofo(definition.pinyin).encode("UTF-8")
            