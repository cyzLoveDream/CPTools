# encoding=utf-8
import json
import re
import random
import jieba
from cpt_untils import ac_detect,build_actree
import numpy as np

class CPTools:
    def ___init__(self):
        pass
    
    def extract_chinese(self, text, symbols= "", remove_letter=False):
        """
         Chinese is extracted and replaced by the provided symbols
        :param text:
        :param symbols:
        :param remove_letter:
        :return:
        
        example:
        cpt = CPTools()
        line = cpt.extract_chinese("我太天真aaa了，想要一切；"," ",remove_letter=True)
        
        """
        if remove_letter:
            rule = re.compile(r"[^\u4e00-\u9fa5]")
        else:
            rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
        line = rule.sub(symbols, text)
        return line
    
    def filter_words_in_corups(self, sensitive_list, raw_text_list):
        
        """
        Filter sensitive words from a large amount of corpus
        :param sensitive_list: the list of sensitive words
        :param raw_text_list: the list of raw corpus
        :return:
        """
        
        actree = build_actree(sensitive_list)
        
        filter_text = []
        for c in raw_text_list:
            if len(ac_detect(actree, c)) == 0:
                filter_text.append(c)
        return filter_text


    def is_chinese(self, uchar):
        """
        
        :param uchar:
        :return:
        """
        if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
            return True
        else:
            return False
    
    def get_json_data(self, path):
        """
        read the file of json with dict of line
        :param path:
        :return:
        """
        return [json.loads(line) for line in open(path, 'r', encoding="utf-8").readlines()]
    
    def save_data_to_npy(self, data, path):
        """
        :param data:
        :param path:
        :return:
        """
        
        np.save(path, data)
        
        print("save finish")
        
    def read_data_from_npy(self, path):
        """
        
        :param path:
        :return:
        """
        return np.load(path).item()
    
    
    
if __name__ == '__main__':
    cpt = CPTools()
    print(cpt.filter_words_in_corups(["我"],["我来了","我走了","来了","走了"]))