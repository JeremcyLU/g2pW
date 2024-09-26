#coding=utf-8
from g2pw import G2PWConverter
from part import separate_pinyin_and_hanzi
import re
import string

def convert_pinyin(input_pinyin):
    tone_marks = {
        'a': 'āáǎà', 'e': 'ēéěè', 'i': 'īíǐì',
        'o': 'ōóǒò', 'u': 'ūúǔù', 'v': 'ǖǘǚǜ'
    }
    
    def apply_tone_mark(syllable, tone):
        if tone == '5':  # 轻声
            return syllable
        for vowel in 'aeiouv':
            if vowel in syllable:
                if vowel == 'i' and 'iu' in syllable:  # 处理 'iu' 的特殊情况
                    return syllable.replace('u', tone_marks['u'][int(tone)-1])
                return syllable.replace(vowel, tone_marks[vowel][int(tone)-1])
        return syllable  # 如果没有元音，返回原始音节
    
    def convert_syllable(syllable):
        if syllable is None:
            return None
        if syllable[-1].isdigit():
            return apply_tone_mark(syllable[:-1], syllable[-1])
        return syllable
    
    return [convert_syllable(syllable) for syllable in input_pinyin if syllable is not None]

def calculate_accuracy(converted, correct):
    paired = [(a, b) for a, b in zip(converted, correct) if a is not None and b != '　']
    total = len(paired)
    correct_count = sum(1 for a, b in paired if a == b)
    accuracy = correct_count / total * 100 if total > 0 else 0
    
    errors = [f"{a},{b}" for a, b in paired if a != b]
    
    return accuracy, errors

import string

def remove_punctuation(hanzis):
    # 定义一个包含所有标点符号的字符串
    punctuation = string.punctuation + '，。！？、；：“”‘’（）《》〈〉【】〔〕…—～·'
    
    # 使用列表推导式去除包含标点符号的元素
    cleaned_hanzis = [s for s in hanzis if all(char not in punctuation for char in s)]
    
    return cleaned_hanzis


def main(correct_pinyin,hanzis):
    # 初始化 G2PWConverter
    conv = G2PWConverter(style='pinyin', model_dir='C:\mzx\pinyin\g2pW\model\G2PWModel', enable_non_tradional_chinese=False)
    
    # 使用 G2PWConverter 生成拼音
    result = conv(hanzis)
    print("G2PWConverter 输出:", result)

    # 提取拼音（排除空的部分）
    input_pinyin = [syllable for sublist in result for syllable in sublist if syllable is not None]

    # 转换拼音
    converted_pinyin = convert_pinyin(input_pinyin)
    print("转换后的拼音:", ','.join(converted_pinyin))

    # 正确的拼音（这里需要你提供正确的拼音，我们暂时使用一个示例）
    # 注意：在实际使用时，你需要为每个输入文本提供相应的正确拼音
    # correct_pinyin = "gòng,gōng,hè,nù,tiān,wéi,zhōng,cuī"  # 请替换为实际的正确拼音
    
    # 计算正确率和错误
    accuracy, errors = calculate_accuracy(converted_pinyin, correct_pinyin)

    print(f"正确率: {accuracy:.2f}%")
    print(f"错误的读音: {', '.join(errors)}")

    hanzis = remove_punctuation(hanzis)
    # print(hanzis)
    # 输出转化错误的文字
    error_chars = []
    for i, (conv, corr) in enumerate(zip(converted_pinyin, correct_pinyin)):
        if conv != corr:
            error_chars.append(hanzis[i])
    
    print("转化错误的文字:", ''.join(error_chars))

if __name__ == '__main__':
    text = "qìng庆lì历sì四nián年chūn春，téng滕zǐ子jīng京zhé谪shǒu守bā巴líng陵jùn郡。yuè越míng明nián年，zhèng政tōng通rén人hé和，bǎi百fèi废jù具xīng兴，nǎi乃chóng重xiū修yuè岳yáng阳lóu楼，zēng增qí其jiù旧zhì制，kè刻táng唐xián贤jīn今rén人shī诗fù赋yú于qí其shàng上，zhǔ属yú予zuò作wén文yǐ以jì记zhī之。jù具 tōng通jù俱　　yú予guān观fú夫bā巴líng陵shèng胜zhuàng状，zài在dòng洞tíng庭yì一hú湖。xián衔yuǎn远shān山，tūn吞cháng长jiāng江，hào浩hào浩shāng汤shāng汤，héng横wú无jì际yá涯，zhāo朝huī晖xī夕yīn阴，qì气xiàng象wàn万qiān千，cǐ此zé则yuè岳yáng阳lóu楼zhī之dà大guān观yě也，qián前rén人zhī之shù述bèi备yǐ矣。rán然zé则běi北tōng通wū巫xiá峡，nán南jí极xiāo潇xiāng湘，qiān迁kè客sāo骚rén人，duō多huì会yú于cǐ此，lǎn览wù物zhī之qíng情，dé得wú无yì异hū乎？　　ruò若fú夫yín淫yǔ雨fēi霏fēi霏，lián连yuè月bù不kāi开，yīn阴fēng风nù怒háo号，zhuó浊làng浪pái排kōng空，rì日xīng星yǐn隐yào曜，shān山yuè岳qián潜xíng形，shāng商lǚ旅bù不xíng行，qiáng樯qīng倾jí楫cuī摧，bó薄mù暮míng冥míng冥，hǔ虎xiào啸yuán猿tí啼。dēng登sī斯lóu楼yě也，zé则yǒu有qù去guó国huái怀xiāng乡，yōu忧chán谗wèi畏jī讥，mǎn满mù目xiāo萧rán然，gǎn感jí极ér而bēi悲zhě者yǐ矣。yǐn隐yào曜 yī一zuò作yǐn隐yào耀；yín淫yǔ雨 tōng通yín霪yǔ雨　　zhì至ruò若chūn春hé和jǐng景míng明，bō波lán澜bù不jīng惊，shàng上xià下tiān天guāng光，yí一bì碧wàn万qǐng顷，shā沙ōu鸥xiáng翔jí集，jǐn锦lín鳞yóu游yǒng泳，àn岸zhǐ芷tīng汀lán兰，yù郁yù郁qīng青qīng青。ér而huò或cháng长yān烟yì一kōng空，hào皓yuè月qiān千lǐ里，fú浮guāng光yuè跃jīn金，jìng静yǐng影chén沉bì璧，yú渔gē歌hù互dá答，cǐ此lè乐hé何jí极！dēng登sī斯lóu楼yě也，zé则yǒu有xīn心kuàng旷shén神yí怡，chǒng宠rǔ辱xié偕wàng忘，bǎ把jiǔ酒lín临fēng风，qí其xǐ喜yáng洋yáng洋zhě者yǐ矣。　　jiē嗟fú夫！yú予cháng尝qiú求gǔ古rén仁rén人zhī之xīn心，huò或yì异èr二zhě者zhī之wéi为，hé何zāi哉？bù不yǐ以wù物xǐ喜，bù不yǐ以jǐ己bēi悲，jū居miào庙táng堂zhī之gāo高zé则yōu忧qí其mín民，chǔ处jiāng江hú湖zhī之yuǎn远zé则yōu忧qí其jūn君。shì是jìn进yì亦yōu忧，tuì退yì亦yōu忧。rán然zé则hé何shí时ér而lè乐yé耶？qí其bì必yuē曰xiān先tiān天xià下zhī之yōu忧ér而yōu忧，hòu后tiān天xià下zhī之lè乐ér而lè乐hū乎！yī噫！wēi微sī斯rén人，wú吾shuí谁yǔ与guī归？　　shí时liù六nián年jiǔ九yuè月shí十wǔ五rì日。"  # 请替换为实际的输入文本
    correct_pinyin, hanzis = separate_pinyin_and_hanzi(text)
    # print(hanzis)
    main(correct_pinyin,hanzis)