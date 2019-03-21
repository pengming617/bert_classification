import numpy as np
from sklearn.metrics import accuracy_score

f = open('data/test.tsv', 'r')
sentences = []
label = []
i = 0
for line in f.readlines():
    if i == 0:
        i += 1
        continue
    line = line.replace("\n", "").split("\t")
    sentences.append(line[1])
    label.append(line[0])
label = [int(x) for x in label]

f = open('tmp/output/test_results.tsv', 'r')
flag = []
for line in f.readlines():
    line = line.replace("\n", "").split("\t")
    scores = [float(x) for x in line]
    index = np.argmax(np.array(scores))
    flag.append(index)
acc = accuracy_score(np.array(label), np.array(flag))
print("acc is:" + str(acc))