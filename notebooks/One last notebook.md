---
jupyter:
  jupytext:
    formats: ipynb,md,py:hydrogen
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.7.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
import pandas as pd
import numpy as np
```

```python
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
df.head()
```

```python
g = df.hist()
```

## this is markdown

```python

```
