"""
    Build Chinese dictionary from text file 
"""
# -*- coding: utf-8 -*-


class dictionary_entry(object):

    def __init__(self, traditional, simplified, pinyin, definition):
        self.traditional = traditional
        self.simplified = simplified
        self.pinyin = pinyin
        self.definition = definition

        
    def __str__(self):
        return  ' \t '.join([self.simplified, self.pinyin, self.definition])
        
dictionary_file = open('cedict_ts.u8' , 'r')

chinese_dictionary = {}

for line in dictionary_file:
    word_traditional = line[0:line.find(" ")]
    word_simplified = line[line.find(" ")+1:line.find(" [")]
    pinyin = line[line.find(" [")+2:line.find("] ")]
    definition = line[line.find(" /")+2:line.find("/ ")-1]
    
    if word_simplified in chinese_dictionary:
        chinese_dictionary[word_simplified].append(dictionary_entry(word_traditional, word_simplified, pinyin, definition))
    else:
        chinese_dictionary[word_simplified] = [ dictionary_entry(word_traditional, word_simplified, pinyin, definition) ]
    
    if word_simplified != word_traditional:
        if word_traditional in chinese_dictionary:
            chinese_dictionary[word_traditional].append(dictionary_entry(word_traditional, word_simplified, pinyin, definition)) #chinese_dictionary[word_simplified]
        else:
            chinese_dictionary[word_traditional] = [ dictionary_entry(word_traditional, word_simplified, pinyin, definition) ] #chinese_dictionary[word_simplified]
    
        
dictionary_file.close()

