# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:21:35 2023

@author: pradyumn
"""

import pandas as pd
df=pd.read_csv("Cutlets.csv")
df.head()
df["Unit A"].mean()
df["Unit B"].mean()
from scipy import stats as twosample
zcal,pval=twosample.ttest_ind(df["Unit A"], df["Unit B"])
print("Z Cal Value:",zcal)
print("P Value:",pval)
alpha=0.05
if pval < alpha:
    print("H1 is accepted And H0 is Rejected")
else:
    print("H0 is accepted and H1 is rejected")