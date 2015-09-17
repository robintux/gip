import string

def init_dict(word_list):
    dic = {}
    for w in word_list:
        dic[w] = w
    return dic

def spelling_errors(word,rule):
    words = []
    for i in range(len(word)):
        if word[i] == rule[0]:
            words.append((word[0:i] + rule[1] + word[i+1:],word))
    return words

def add_corrections(dic,rules):
    words = dic.keys()
    for word in words:
        for rule in rules:
            dic.update(spelling_errors(word,rule))

def spelling_corrector(text,dic):
    words = text.split()
    corrected_words = [dic[word] for word in words]
    return string.join(corrected_words)

text = 'hwre ww sre in thr centrr pf tpwn'
words_in_dictionary = ['here','we','are','in','the','center','of','town']
rules = [('e','r'),('e','w'),('a','s'),('o','p')]
dic = init_dict(words_in_dictionary)
add_corrections(dic,rules)
print(spelling_corrector(text,dic))

 
