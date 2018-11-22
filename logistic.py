import math
import numpy as np
from random import random
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.model_selection import StratifiedShuffleSplit


def make_x():
    return [i / 100 for i in range(-2000,2000,1)]


def logit(x, w0, w1):
    return 1 / (1 + math.exp(-(x * w1 + w0)))


def plot_logistic(w0, w1):
    x = make_x()
    y = [logit(i, w0, w1) for i in x]
    # print(y)
    plt.plot(x, y, linewidth=2, label='w0={:.2f},w1={:.2f}'.format(w0, w1))
    plt.legend()


def sharp_edge(x, border=0):
    if x >= border:
        return 1
    else:
        return 0


def generate_random_bin(p):
    if p >= random():
        return 1
    else:
        return 0


def generate_data_fit_to_log_reg(w1):
    x = make_x()
    y = [generate_random_bin(logit(i, 0, w1)) for i in x]
    X = np.matrix(x).reshape(4000, 1)
    Y = np.array(y).reshape((4000, 1))
    return X, Y


def fit_for_one_bs_iter(clf, sss, X, Y, w1):
    for (tri, tei) in sss.split(X, Y):
        xtr, ytr = X[tri], Y[tri].ravel()
        xte, yte = X[tei], Y[tei].ravel()
        xte_flat = xte.reshape(xte.shape[0]).tolist()[0]
        clf.fit(xtr, ytr)
        y_pred_proba = clf.predict_proba(xte)
        auc = roc_auc_score(yte, y_pred_proba[:,1])
        mse = mean_squared_error([logit(x, 0, w1) for x in xte_flat], y_pred_proba[:,1])
    return clf.intercept_[0], clf.coef_[0][0], auc, mse


def calculate_outputs_of_logreg(clf, X, Y, w1, n_samples):
    sss = StratifiedShuffleSplit(n_splits=2, train_size=0.5, test_size=0.5)
    d = []
    for n in range(n_samples):
        d.append(fit_for_one_bs_iter(clf, sss, X, Y, w1))

    outputs = pd.DataFrame(d, columns=['w0', 'w1', 'auc', 'mse'])
    param_values = pd.concat([
        outputs.mean().rename('means'),
        (2 * outputs.std() / math.sqrt(n_samples)).rename('conf_ints')
    ], axis=1)
    return param_values

