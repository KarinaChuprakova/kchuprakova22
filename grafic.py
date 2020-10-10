#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #подключение модуля
import numpy #подключение модуля
import matplotlib.pyplot as mpp #подключение модуля

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': #введелние модуля как переменной
    arguments = numpy.r_[0:200:0.1] #задавание областей значения и определения
    mpp.plot( #введение зависимости у от x
        arguments, #значения аргумента
        [math.sin(a) * math.sin(a/20.0) for a in arguments] #зависимость у от аргумента
    )
    mpp.show() #вывод графика на экране