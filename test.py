#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/18
"""
"""
from phkit import text2phoneme, text2sequence, symbol_chinese
from phkit import chinese_sequence_to_text, chinese_text_to_sequence

def test_phkit():
    from phkit import text2phoneme, text2sequence, symbol_chinese
    from phkit import chinese_sequence_to_text, chinese_text_to_sequence
    text = "汉字转音素，TTS：《Text to speech》。"
    target_ph = ['h', 'an', '4', '-', 'z', 'iy', '4', '-', 'zh', 'uan', '3', '-', 'ii', 'in', '1', '-', 's', 'u', '4', '-', ',', '-',
              'Tt', 'Tt', 'Ss', '-', ':', '-', '(', '-', 'T', 'E', 'X', 'T', '-', '#', '-', 'T', 'O', '-', '#', '-', 'S', 'P', 'E', 'E', 'C', 'H', '-', ')', '-', '.', '-', '~', '_']

    result = text2phoneme(text)
    assert result == target_ph

    target_seq = [11, 32, 74, 2, 28, 51, 74, 2, 29, 59, 73, 2, 12, 46, 71, 2, 22, 56, 74, 2, 131, 2, 95, 95, 94, 2, 133, 2, 136, 2, 121,
              106, 125, 121, 2, 135, 2, 121, 116, 2, 135, 2, 120, 117, 106, 106, 104, 109, 2, 137, 2, 130, 2, 1, 0]

    result = text2sequence(text)
    assert result == target_seq

    result = chinese_text_to_sequence(text)
    assert result == target_seq

    target_ph = ' '.join(target_ph)
    result = chinese_sequence_to_text(result)
    assert result == target_ph

    assert len(symbol_chinese) == 145

    text = "岂有此理"
    target = ['q', 'i', '2', '-', 'ii', 'iu', '3', '-', 'c', 'iy', '2', '-', 'l', 'i', '3', '-', '~', '_']
    result = text2phoneme(text)

    assert result == target


def text2phoneme2(text):
    ph = text2phoneme(text)
    # print(ph)
    result = "sil"
    for item in ph:
        converted_c = ''
        if item in ['1', '2', '3', '4', '5']:
            converted_c = item
        elif item in ['-']:
            converted_c = ' '
        elif item not in ['~', '_']:
            result = result.strip(' ')
            converted_c = ' ' + item
        if converted_c != '':
            result += converted_c
    result = result.strip(' ')
    result += ' sil'
    return result


def test_phkit_bb():
    text = "汉字转音素"
    text = "这场抗议活动究竟是如何发展演变的 又究竟是谁伤害了谁"

    texts = [
        "学校深入实施人才强校战略", "深化人事制度改革", "教职工队伍整体水平显著提高", "为学校各项事业发展奠定了坚实基础",
        "世界一流大学建设取得了历史性进步", "有一流的教师才有一流的教育", "才能培养出一流的人才", "强化教职工队伍建设的主体责任",
        "作为新时代的清华教师", "为培养德智体美劳全面发展的社会主义建设者和接班人作出新的贡献",
        "谢谢", "再见", "对不起", "请拿好杯子", "谢谢再见对不起"
    ]
    results = []
    for text in texts:
        result = text2phoneme2(text)
        results.append(result)
        print(text)
        print(result)
    print(results)


if __name__ == "__main__":
    print(__file__)
    test_phkit_bb()
