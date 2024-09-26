def convert_pinyin(input_pinyin):
    # 声调到声调符号的映射
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
            return '　'  # 使用全角空格
        if syllable[-1].isdigit():
            return apply_tone_mark(syllable[:-1], syllable[-1])
        return syllable
    
    return [convert_syllable(syllable) for syllable in input_pinyin]

def calculate_accuracy(converted, correct):
    total = len(converted)
    correct_count = sum(1 for a, b in zip(converted, correct) if a == b)
    accuracy = correct_count / total * 100
    
    errors = [f"{a},{b}" for a, b in zip(converted, correct) if a != b and a != '　' and b != '　']
    
    return accuracy, errors

# 测试代码
input_pinyin = ['gong1', 'gong1', 'he4', 'nu4', None, 'tian1', 'wei2', 'zhong1', 'cui1', None, None, 'kun1', 'jing1', 'pen1', 'dang4', None, 'yang2', 'tao2', 'qi3', 'lei2', None, None, 'yu2', 'long2', 'xian4', 'ren2', None, 'cheng2', 'ci3', 'huo4', 'tai1', None, None, 'huo3', 'fen2', 'kun1', 'shan1', None, 'yu4', 'shi2', 'xiang1', 'dui1', None, None, 'yang3', 'xi1', 'lin2', 'yu3', None, 'sa3', 'bao3', 'yan2', 'wei1', None, None, 'jian4', 'fa1', 'shi2', 'kai1', None, 'ge1', 'hui1', 'ri4', 'hui2', None, None, 'zou1', 'yan3', 'tong4', 'ku1', None, 'yan4', 'shuang1', 'sa4', 'lai2', None, None, 'wei2', 'cheng2', 'bu4', 'gan3', None, 'you2', 'zhi2', 'xia4', 'tai2', None, None, 'cang1', 'ying1', 'bo2', 'jue2', None, 'dan1', 'ji2', 'cui1', 'wei2', None, None, 'hao2', 'sheng4', 'diao1', 'ku1', None, 'wang2', 'feng1', 'shang1', 'ai1', None, None, 'si1', 'wen2', 'wei4', 'sang4', None, 'dong1', 'yue4', 'qi3', 'tui2', None, None, 'mu4', 'tao2', 'chu3', 'nan4', None, 'zou1', 'tuo1', 'wu2', 'zai1', None, None, 'jian4', 'ji1', 'ku3', 'chi2', None, 'er4', 'gong1', 'suo3', 'hai1', None, None, 'ji4', 'bu2', 'zou4', 'jin4', None, 'lin2', 'he2', 'lai2', 'zai1', None, None, 'xing1', 'li2', 'yi4', 'men2', None, 'cao3', 'zhi2', 'er4', 'hai2', None, None, 'wan4', 'fen4', 'jie2', 'qi4', None, 'you1', 'cong2', 'zhong1', 'cui1', None, None, 'jin1', 'se4', 'yu4', 'hu2', None, 'jin4', 'wei2', 'chou2', 'mei2', None, None, 'ju3', 'jiu3', 'tai4', 'xi2', None, 'qi4', 'xie3', 'ying2', 'bei1', None, None, 'tai2', 'xing1', 'zai4', 'lang3', None, 'tian1', 'wang3', 'chong2', 'hui1', None, None, 'qu1', 'fa3', 'shen1', 'en1', None, 'qi4', 'xia2', 'qu3', 'cai2', None, None, 'ye3', 'chang2', 'fei1', 'zui4', None, 'ni2', 'fu4', 'wu2', 'cai1', None, None, 'fu4', 'pen2', 'tang3', 'ju3', None, 'ying4', 'zhao4', 'han2', 'hui1', None]

converted_pinyin = convert_pinyin(input_pinyin)
correct_pinyin = "gōng,gōng,hè,nù,　,tiān,wéi,zhōng,cuī,　,　,kūn,jīng,pēn,dàng,　,yáng,táo,qǐ,léi,　,　,yú,lóng,xiàn,rén,　,chéng,cǐ,huò,tāi,　,　,huǒ,fēn,kūn,shān,　,yù,shí,xiāng,duī,　,　,yǎng,xī,lín,yǔ,　,sǎ,bǎo,yán,wēi,　,　,jiàn,fā,shí,kāi,　,gē,huī,rì,huí,　,　,zōu,yǎn,tòng,kū,　,yàn,shuāng,sǎ,lái,　,　,wéi,chéng,bù,gǎn,　,yóu,zhí,xià,tái,　,　,cāng,yīng,bó,jué,　,dān,jí,cuī,wéi,　,　,háo,shèng,diāo,kū,　,wáng,fēng,shāng,āi,　,　,sī,wén,wèi,sàng,　,dōng,yuè,qǐ,tuí,　,　,mù,táo,chǔ,nàn,　,zōu,tuō,wú,zāi,　,　,jiàn,jī,kǔ,chí,　,èr,gōng,suǒ,hāi,　,　,jì,bú,zǒu,jìn,　,lín,hé,lái,zāi,　,　,xīng,lǐ,yì,mén,　,cǎo,zhí,ér,hái,　,　,wàn,fèn,jié,qì,　,yōu,cóng,zhōng,cuī,　,　,jīn,sè,yù,hú,　,jìn,wéi,chóu,méi,　,　,jǔ,jiǔ,tài,xǐ,　,qì,xiě,yíng,bēi,　,　,tái,xīng,zài,làng,　,tiān,wǎng,chóng,huī,　,　,qū,fǎ,shēn,ēn,　,qì,xiá,qǔ,cái,　,　,yě,cháng,fēi,zuì,　,ní,fù,wú,cāi,　,　,fù,pén,tǎng,jǔ,　,yìng,zhào,hán,huī,　".split(',')

accuracy, errors = calculate_accuracy(converted_pinyin, correct_pinyin)

print(f"转换后的拼音: {','.join(converted_pinyin)}")
print(f"正确率: {accuracy:.2f}%")
print(f"错误的读音: {', '.join(errors)}")