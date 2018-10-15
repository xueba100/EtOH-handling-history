# -*- coding: utf-8 -*-
#This script returns to scatter plot of data.
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy
import csv

#数据载入
csv_path = input("Give me a csv file name. eg.H:\DataSet\EEG\\alcoholics\co2a0000364\co2a0000364-000.csv\n")
train_data = pd.read_csv(csv_path)

#数据构成分析
train_data.info()
train_data.head()
train_data.tail()

#数据基本统计学分析

