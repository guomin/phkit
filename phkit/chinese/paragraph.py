#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: guom06
# date: 2020/10/22
"""
#### paragraph
段落，多句子处理

"""
import os
import re


def _preprocess(text, tone=False):
    if not tone:
        text = re.sub(r'#\d+', '', text)

    text = text.lower()
    text = re.sub(r'[）（]', '', text)
    text = text.replace('：“', '，').replace('：', '，').replace('”！', '！').replace('”。', '。')
    text = text.replace('……”', '。').replace('……', '。').replace('…。', '。').replace('…”', '。').replace('…', '。').replace(
        '.', '。')
    text = text.replace('”', '').replace('“', '').replace('、', '，').replace('-', '，')
    text = text.replace('—', '，').replace('-', '，').replace('；', '。')
    text = re.sub(r'，[，\s]+', '，', text)
    text = re.sub(r'。[。，\s]+', '。', text)
    text = re.sub(r'，。+', '。', text)

    text = re.sub(r'？[？\s]+', '？', text)
    text = re.sub(r'，？+', '？', text)

    text = re.sub(r'！[！\s]+', '！', text)
    text = re.sub(r'，！+', '！', text)
    text = re.sub('\.+', '。', text)
    text = re.sub(',+', '，', text)
    text = re.sub('!+', '！', text)
    text = re.sub('\?+', '？', text)

    text = re.sub(r'\s+', ' ', text)
    text = text.replace('|', '')
    text = text.strip()
    return text


def split2sentence(text):
    text = _preprocess(text)
    return [s for s in re.split(r'[,!，。！“”""……]', text) if len(s) > 0]

