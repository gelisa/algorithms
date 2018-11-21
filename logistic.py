import math
import numpy as np
from random import random


def make_x():
    return [i / 100 for i in range(-2000,2000,1)]


def logit(x, b, w0, w1):
    return 1 / (1 + math.exp( -math.log(b) * (x * w1 + w0)))


def generate_random_bin(p):
    if p >= random():
        return 1
    else:
        return 0


def predict_w1(clf, w1):
    x = make_x()
    y = [generate_random_bin(logit(i, math.exp(1), 0, w1)) for i in x]
    X = np.matrix(x).reshape(4000, 1)
    Y = np.array(y).reshape((4000,))
    clf.fit(X, Y)
    return w1, clf.coef_[0][0]

