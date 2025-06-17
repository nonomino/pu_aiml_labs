import numpy as np
import math
import gensim.downloader

model = gensim.downloader.load("glove-wiki-gigaword-50")

def vec(w): return model[w]
def dot(v1, v2): return np.dot(v1, v2)
def length(v): return math.sqrt(dot(v, v))
def cosim(v1, v2): return dot(v1, v2) / (length(v1) * length(v2))

print(vec('queen'))
print(model.most_similar('queen')[0][0])
print(cosim(vec('man'), vec('woman')))
print("Difference in similarity =", abs(cosim(vec('man'), vec('woman')) - cosim(vec('men'), vec('women'))))
print(model.most_similar(positive=['men', 'woman'], negative=['man'])[0][0])

def complete_mcq_analogy(wordA, wordB, wordC, options):
  target = vec(wordC) + vec(wordB) - vec(wordA)
  return max(options, key=lambda opt: cosim(target, vec(opt)))

print(complete_mcq_analogy('insect', 'disease', 'war', ['arsenal','defeat','army','destruction','trench']))

def complete_analogy(wordA, wordB, wordC):
  target = vec(wordC) + vec(wordB) - vec(wordA)
  return model.most_similar([target], topn=1)[0][0]
