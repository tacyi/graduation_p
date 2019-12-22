#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 18:38
# @Author  : tacyi
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
from scipy.io import wavfile
import os


# 画短时傅里叶声谱图并保存图片，代码相关参考链接https://blog.csdn.net/qq7835144/article/details/88887576，

# 最主要的疑问是我不确定
# (sample_rate, x) = wavfile.read(rd)中的总采样数x是否是
# signal.stft(x, **params)的参数x;官方给了例子我看的很懵懂。

# 官方链接https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.stft.html#scipy.signal.stft
# 下面是我的实现
def stft_specgram(g, n, **params):
    rd = 'C:/Users/tacyi/Desktop/genres/' + g + '/' + g + '.' + str(n).zfill(5) + '.wav'

    # 主要深究的函数有下面几个
    (sample_rate, x) = wavfile.read(rd)
    # f: 采样频率数组；t: 时间数组；Zxx: STFT结果
    f, t, zxx = signal.stft(x, **params)
    plt.pcolormesh(t, f, np.abs(zxx))
    plt.colorbar()
    plt.title('STFT Magnitude')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    # plt.tight_layout(pad=0)
    plt.tight_layout()

    sd = './picture/STFT/' + g
    if not os.path.exists(sd):
        os.makedirs(sd)

    sp = './picture/STFT/' + g + '/' + g + '.' + str(n).zfill(5) + '.png'
    # if sp is not None:
    if not os.path.exists(sp):
        plt.savefig(sp)  # 保存图像
    plt.clf()  # 清除画布
    # return t, f, zxx


genre_list = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
for g in genre_list:
    for n in range(100):
        stft_specgram(g, n)
