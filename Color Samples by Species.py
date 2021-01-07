#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  os
os.getcwd() #获取当前工作目录路径


# In[2]:


# To process data.
import pandas as pd
import numpy as np
# To plot.
from pylab import *
from plotnine import *


# In[3]:


df = pd.read_csv('/mnt/c/Users/Files/10x/1223/gem_classification.csv')


# In[4]:


df.head(5)


# In[5]:


# geom_point. Reorder GelBead_TrueSeq by Reads.
(ggplot(df, aes(x = 'GRCh38', y = 'mm10', color = 'factor(call)' ) )
+ geom_point()
#+ scale_alpha_continuous(range=(1,100))
+ labs(x='GRCh38 UMI counts', y='mm10 UMI counts', title = "Cell UMI Counts")
+ theme_bw()
+ theme(panel_grid=element_blank())
)

