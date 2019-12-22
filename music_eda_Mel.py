#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 12:48
# @Author  : tacyi

import os
import librosa
import librosa.display
import matplotlib.pyplot as plt


# 画梅尔声谱图并保存图片。请老师你看看是否正确
def mel_specgram(g, n, **params):
    rd = 'C:/Users/tacyi/Desktop/genres/' + g + '/' + g + '.' + str(n).zfill(5) + '.wav'

    # 主要深究的函数有下面几个
    y, sr = librosa.load(rd, sr=None)
    # 等同写法melspec = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)
    melspec = librosa.feature.melspectrogram(y, sr, **params)
    logmelspec = librosa.power_to_db(melspec)
    librosa.display.specshow(logmelspec, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar()

    sd = './picture/Mel/' + g
    if not os.path.exists(sd):
        os.makedirs(sd)
    sp = './picture/Mel/' + g + '/' + g + '.' + str(n).zfill(5) + '.png'
    # if sp is not None:
    if not os.path.exists(sp):
        plt.savefig(sp)  # 保存图像
    plt.clf()  # 清除画布


genre_list = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
for g in genre_list:
    for n in range(100):
        mel_specgram(g, n, n_fft=1024, hop_length=512, n_mels=128)
