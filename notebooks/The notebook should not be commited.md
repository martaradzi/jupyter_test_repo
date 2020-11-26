```python
!pip3 install pandas
!pip3 install numpy
```

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

# This is a test markdown 

```python
df.describe()
```

```python

```
