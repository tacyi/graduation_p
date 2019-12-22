#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 18:38
# @Author  : tacyi
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
from scipy.io import wavfile
import os

# #################### 这个脚本是没用的 #################################


# import wavio
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy import signal
# path="C:/Users/tacyi/Desktop/genres/blues/blues.00000.wav"
# wav_struct = wavio.read(path)
# wav = wav_struct.data.astype(float) / np.power(2, wav_struct.sampwidth * 8 - 1)
# [f, t, X] = signal.spectral.spectrogram(wav, np.hamming(1024), nperseg=1024, noverlap=0, detrend=False,
#                                         return_onesided=True, mode='magnitude')
# plt.pcolormesh(t, f, np.abs(X))
# plt.colorbar()
# plt.title('STFT Magnitude')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.tight_layout()
# plt.show()


(sample_rate, x) = wavfile.read("C:/Users/tacyi/Desktop/genres/blues/blues.00000.wav")
print(sample_rate, x.shape)
# #
# #
# # def stft_specgram(x, picname=None, **params):  # picname是给图像的名字，为了保存图像
# #     f, t, zxx = signal.stft(x, **params)
# #     plt.pcolormesh(t, f, np.abs(zxx))
# #     plt.colorbar()
# #     plt.title('STFT Magnitude')
# #     plt.ylabel('Frequency [Hz]')
# #     plt.xlabel('Time [sec]')
# #     plt.tight_layout()
# #     if picname is not None:
# #         plt.savefig('./' + str(picname) + '.jpg')  # 保存图像
# #     plt.clf()  # 清除画布
# #     return t, f, zxx


# stft_specgram(x, '000')
