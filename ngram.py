import nltk
from nltk.util import ngrams
import operator

def word_grams(words, n):
    grams = {}
    for pair in ngrams(words, n):
        if pair not in grams:
            grams[pair] = 1
        else:
            grams[pair] += 1
    return grams
def prob(grams):
    grams_prob = grams.copy()
    d = sum(grams.values())
    for gram in grams_prob:
        grams_prob[gram] = grams_prob[gram]/d
    return grams_prob

#Quiz 2-1
def ngram_probs(filenme='data/raw_sentences.txt'):
    with open('data/raw_sentences.txt', 'r') as f:
        w = ' '.join(s.strip().lower() for s in f.readlines())
    bigrams = word_grams(w.split(' '),2)
    trigrams = word_grams(w.split(' '),3)
    return prob(bigrams),prob(trigrams)

#Quiz 2-2
def prob3(bigram, cnt2=cnt2, cnt3=cnt3):
    if bigram not in cnt2: return None
    else : prob = cnt2[bigram]
    next_word_prob = {}
    for p in cnt3:
        if p[:2]==bigram: 
            next_word_prob[p[2]] = cnt2[bigram]/cnt3[p]
    return next_word_prob

#Quiz 2-3
def predict_max(starting, cnt2=cnt2, cnt3=cnt3):
    sentence = []
    sentence.append(starting)
    while True:
        next_word_prob = prob3(starting)
        next_word = max(next_word_prob.items(), key=operator.itemgetter(1))[0]
        sentence.append(next_word)
        if len(sentence) < 15 and next_word != ".":
            starting = (starting[1],next_word)
        else:
            break
    return sentence

