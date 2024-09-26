import string

import string

def remove_punctuation(hanzis):
    # 定义一个包含所有标点符号的字符串
    punctuation = string.punctuation + '，。！？、；：“”‘’（）《》〈〉【】〔〕…—～·'
    
    # 使用列表推导式去除包含标点符号的元素
    cleaned_hanzis = [s for s in hanzis if all(char not in punctuation for char in s)]
    
    return cleaned_hanzis

# 示例列表
hanzis = ['你好，世界！', '这是测试。', '（括号）', '标点:;!?']

# 调用函数并打印结果
cleaned_hanzis = remove_punctuation(hanzis)
print(cleaned_hanzis)