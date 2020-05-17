import jsonlines
from collections import Counter
from pprint import pprint


def print_dtypes(kind):
    data = jsonlines.Reader(open('C:/Users/mrper/Desktop/24[7]ai/GettingToKnowYou-master/data/dialogue_nli/dialogue_nli_%s.jsonl' % kind, 'r')).read()
    dtype_counts = Counter([(d['dtype'], d['label']) for d in data])
    print('--- %s (%d) ---' % (kind, len(data)))
    pprint(dict(dtype_counts))
    print('')


if __name__ == '__main__':
    print_dtypes('train')
    print_dtypes('dev')
    print_dtypes('test')
