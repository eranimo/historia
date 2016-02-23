import random

VOWELS = 'a,e,i,o,u'.split(',')
CONSONANTS = 'b,c,d,f,g,h,j,k,l,m,n,p,r,s,t,v,w,x,y,z'.split(',')
COMMON = 'd c d f g h l m n r s t'.split(' ')
DOUBLES = ['th', 'ng', 'ge', 'ch', 'dg']
LONGS = [v1+v2 for v2 in VOWELS for v1 in VOWELS if v2 != v1]

# https://czone.eastsussex.gov.uk/sites/gtp/library/core/english/Documents/phonics/Table%20of%20phonemes.pdf

KEYS = {
    'C': CONSONANTS,
    'V': VOWELS,
    'D': DOUBLES,
    'K': COMMON,
    'L': LONGS
}

PATTERNS = ['KLKL'] * 1 + \
           ['KLKV'] * 5 + \
           ['KVKVKV'] * 3 + \
           ['KLD'] * 1

def random_word():
    pattern = random.choice(PATTERNS)
    word = ''
    for index in pattern:
        word += random.choice(KEYS[index])
    return word


if __name__ == '__main__':
    for i in xrange(50):
        print(random_word())
