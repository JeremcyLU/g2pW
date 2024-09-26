def separate_pinyin_and_hanzi(text):
    pairs = text.split()
    pinyins = []
    hanzis = []
    
    for pair in pairs:
        pinyin = ''
        hanzi = ''
        for char in pair:
            if '\u4e00' <= char <= '\u9fff':  # 汉字的Unicode范围
                if pinyin:
                    pinyins.append(pinyin)
                    pinyin = ''
                hanzi += char
            elif char in ['，', '；', '？', '！','、','。']:  # 标点符号
                if hanzi:
                    hanzis.append(hanzi)
                    hanzi = ''
                hanzi += char
            else:
                if hanzi:
                    hanzis.append(hanzi)
                    hanzi = ''
                pinyin += char
        if pinyin:
            pinyins.append(pinyin)
        if hanzi:
            hanzis.append(hanzi)
    
    return pinyins, hanzis

def main():
    input_text = """guān关guān关jū雎jiū鸠，zài在hé河zhī之zhōu洲。yǎo窈tiǎo窕shū淑nǚ女，jūn君zǐ子hǎo好qiú逑。cēn参cī差xìng荇cài菜，zuǒ左yòu右liú流zhī之。yǎo窈tiǎo窕shū淑nǚ女，wù寤mèi寐qiú求zhī之。qiú求zhī之bù不dé得，wù寤mèi寐sī思fú服。yōu悠zāi哉yōu悠zāi哉，zhǎn辗zhuǎn转fǎn反cè侧。cēn参cī差xìng荇cài菜，zuǒ左yòu右cǎi采zhī之。yǎo窈tiǎo窕shū淑nǚ女，qín琴sè瑟yǒu友zhī之。cēn参cī差xìng荇cài菜，zuǒ左yòu右mào芼zhī之。yǎo窈tiǎo窕shū淑nǚ女，zhōng钟gǔ鼓lè乐zhī之。"""

    pinyins, hanzis = separate_pinyin_and_hanzi(input_text)

    print("拼音:")
    print(','.join(pinyins))
    print("\n汉字:")
    print(''.join(hanzis))

if __name__ == "__main__":
    main()
