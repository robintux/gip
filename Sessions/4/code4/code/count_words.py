import urllib
from operator import itemgetter

def main():
    genesis = urllib.urlopen('http://www.gutenberg.org/cache/epub/8001/pg8001.txt')
    alice = urllib.urlopen('http://www.gutenberg.org/cache/epub/11/pg11.txt')

    n = 30
    print_most_popular(genesis, n, 'Genesis')
    print_most_popular(alice, n, 'Alice In Wonderland')

def main1():
    n = 5
    for bible_num in range(8001,8006):
        url = 'http://www.gutenberg.org/cache/epub/' + str(bible_num) + '/pg'  + str(bible_num) + '.txt'
        book = urllib.urlopen(url)
        print_most_popular(book, n, url)

    for alice_num in range(11,14):
        url = 'http://www.gutenberg.org/cache/epub/' + str(alice_num) + '/pg'  + str(alice_num) + '.txt'
        book = urllib.urlopen(url)
        print_most_popular(book, n, url)


def print_most_popular(url,n, book_name):
    ''' url - text
        n - num of popular words to print
        book_name - name of book
    '''
    text = url.read()    
    words = text.split()    

    dic = {}
    for w in words:
        dic[w] = dic.get(w, 0) + 1        

    sorted_words = sorted(dic.items(), key=itemgetter(1), reverse=True)    
    popular_words = sorted_words[0:n]
    popular_words_count = 0
    for word, count in popular_words:
        popular_words_count += count

    print '*****', book_name, '*****'
    for word, count in popular_words:
        print word, '-->', float(count)/popular_words_count

main1()


