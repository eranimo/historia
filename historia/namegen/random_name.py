import random

vowels = ["a", "e", "i", "o", "u", "y"]
dipthongs = ['ae', 'ia', 'io', 'oa', 'ea', 'ua']
consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w",
    "th"
]
endings = ['ia', 'ium']
initial = ['th', 'gr', 'de', 'da', 'ye', 'sa', 'fe', 'fa', 've', 'be', 'bra', 'gr']
medial = ['iz', 'ea', 'ae', 'ha', 'ar', 'cu', 'pe', 'ca']
final = ['io', 'ia', 'er', 'ium']

symbols = {
    'V': vowels,
    'C': consonants,
    'D': dipthongs,
    'I': initial,
    'F': final,
    'M': medial,
    'E': endings
}

PATTERNS = [
    'IF',
    'IMF',
    'IMMF'
]

def make_name():
    pattern = random.choice(PATTERNS)
    return ''.join([random.choice(symbols.get(i)) for i in list(pattern)])

if __name__ == '__main__':
    for i in range(10):
        print(make_name())
