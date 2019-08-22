# -*- coding:utf-8 -*-

import numpy as np

def perceptron_hinge_loss(w: np.array, x: np.array, t: np.array) -> float:
    '''
    @param w: 重みベクトル
    @param x: 入力ベクトル
    @param t: 正解ラベル(1か-1)
    @return loss: ヒンジ損失(Hinge Loss)
    '''
    loss = 0
    for input, label in zip(x, t):
        v = label * np.dot(w, input)
        loss += max(0, -v)
    return loss

def predict(w: np.array, x: np.array) -> int:
    '''
    @param w: 重みベクトル
    @param x: 入力ベクトル
    @return: クラスの正負(1, -1)
    '''
    sum = np.dot(w, x)
    if sum >= 0:
        return 1
    else:
        return -1

def job():
    w = np.array([2, 3])
    x = np.array(([4, 2], [2,5]))
    t = np.array((1, -1))

    loss = perceptron_hinge_loss(w, x, t)
    print('loss', loss)
    for xi in x:
        predict_value = predict(w, xi)
        print('predict', predict_value)
    return