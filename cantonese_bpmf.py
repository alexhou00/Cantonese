# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:44:26 2023

@author: alexh
"""

from pyjyutping.jyutping import convert as to_jyutping
import re

jyutping_bpmf_dict = {
 'b': 'ㄅ',
 'p': 'ㄆ',
 'm': 'ㄇ',
 'f': 'ㄈ',
 'd': 'ㄉ',
 't': 'ㄊ',
 'n': 'ㄋ',
 'l': 'ㄌ',
 'g': 'ㄍ',
 'k': 'ㄎ',
 'ng': 'ㄫ',
 'h': 'ㄏ',
 'gw': 'ㄍㄨ',
 'kw': 'ㄎㄨ',
 'z': 'ㄗ',
 'c': 'ㄘ',
 's': 'ㄙ',
 'j': 'ㄧ',
 'w': 'ㄨ',
 'aa': 'ㄚ',
 'aai': 'ㄞ',
 'aau': 'ㄠ',
 'aam': 'ㄚㄇ',
 'aan': 'ㄢ',
 'aang': 'ㄤ',
 'aap': 'ㄚㄅ',
 'aat': 'ㄚㄉ',
 'aak': 'ㄚㄍ',
 'ai': 'ハㄧ',
 'au': 'ハㄨ',
 'am': 'ハㄇ',
 'an': 'ハㄣ',
 'ang': 'ハㄥ',
 'ap': 'ハㄅ',
 'at': 'ハㄉ',
 'ak': 'ハㄍ',
 'e': 'ㄝ',
 'ei': 'ㄟ',
 'eu': 'ㄝㄨ',
 'em': 'ㄝㄇ',
 'en': 'ㄝㄣ',
 'eng': 'ㄝㄥ',
 'ep': 'ㄝㄅ',
 'et': 'ㄝㄉ',
 'ek': 'ㄝㄍ',
 'i': 'ㄧ',
 'iu': 'ㄧㄨ',
 'im': 'ㄧㄇ',
 'in': 'ㄧㄣ',
 'ing': 'ㄧㄥ',
 'ip': 'ㄧㄅ',
 'it': 'ㄧㄉ',
 'ik': 'ㄧㄍ',
 'o': 'ㄛ',
 'oi': 'ㄛㄧ',
 'ou': 'ㄡ',
 'on': 'ㄛㄣ',
 'ong': 'ㄛㄥ',
 'ot': 'ㄛㄉ',
 'ok': 'ㄛㄍ',
 'oe': 'サ',
 'eoi': 'ㄜㄩ',
 'eon': 'ㄜㄣ',
 'oeng': 'サㄥ',
 'eot': 'ㄜㄉ',
 'oek': 'サㄍ',
 'u': 'ㄨ',
 'ui': 'ㄨㄧ',
 'un': 'ㄨㄣ',
 'ung': 'ㄨㄥ',
 'ut': 'ㄨㄉ',
 'uk': 'ㄨㄍ',
 'yu': 'ㄩ',
 'yun': 'ㄩㄣ',
 'yut': 'ㄩㄉ',
 'jung': 'ㄩㄥ', # special rule
 '1': 'ˉ', '2': 'ˊ', '3': '˫', '4': 'ˇ', '5': '˘', '6': '˪'} # tones

def is_chinese_char(char):
    """Check if a character is a Chinese character"""
    punc = "，。、．？！：；・・‥…—～〜／＼＿〃―‖「」『』〔〕【】《》﹁﹂﹃﹄︹︺︻︼︽︾（）｛｝〈〉〖〗︵︶︷︸︿﹀"
    return '\u4e00' <= char <= '\u9fff' and char not in punc

def jyutping_to_bpmf(jyutping):
    bpmf = jyutping
    for k, v in jyutping_bpmf_dict_sorted.items():
        bpmf = bpmf.replace(k, v)

    special_handling = {
     'ㄗㄧ': 'ㄐㄧ',
     'ㄘㄧ': 'ㄑㄧ',
     'ㄙㄧ': 'ㄒㄧ',
     'ㄗㄩ': 'ㄐㄩ',
     'ㄘㄩ': 'ㄑㄩ',
     'ㄙㄩ': 'ㄒㄩ',
     'ㄧㄩ': 'ㄩ',  # jyu -> ㄩ
     'ㄧㄧ': 'ㄧ',  # ji -> ㄧ
     'ㄨㄨ': 'ㄨ'  # wu -> ㄨ
     }

    for k, v in special_handling.items():
        bpmf = bpmf.replace(k, v)
        
    return bpmf

jyutping_bpmf_dict_sorted = dict(sorted(jyutping_bpmf_dict.items(), key=lambda x: len(x[0]), reverse=True))

input_str = input("Enter Jyutping or Chinese characters: ")


jyutping = to_jyutping(input_str)
bpmf = []
for word in jyutping.split(' '):
    if re.match(r'[a-zA-Z]{1,6}\d', word):  # If match a jyutping word pattern
        bpmf.append(jyutping_to_bpmf(word.lower()))
    else:
        bpmf.append(word)


print(' '.join(bpmf))