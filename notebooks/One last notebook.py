# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import numpy as np

# %%
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
df.head()

# %%
g = df.hist()

# %% [markdown]
# ## this is markdown

# %%
