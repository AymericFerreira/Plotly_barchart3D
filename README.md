# Plotly 3D barchart
Plotly doesn't provide a simple way to create 3D barcharts as matplotlib does.
Here is a function to create them easily via Mesh3D, inspired by *empet* post (https://community.plotly.com/t/how-to-do-a-3d-bar-chart-if-possible/32287/2)

Some examples : 

Minimal example

```
from barchart import plotly_barcharts_3d
import pandas as pd

xdf = pd.Series([1, 1, 10, 10])
ydf = pd.Series([2, 4, 2, 4])
zdf = pd.Series([10, 30, 20, 45])

fig = plotly_barcharts_3d(xdf, ydf, zdf, color='x+y')
fig.show()
```
![Image small xy](https://github.com/AymericFerreira/Plotly_barchart3D/blob/master/examples/small_xy.png?raw=true)

It can also be use to generate bigger graph and add legends.
```
from barchart import plotly_barcharts_3d
import pandas as pd

df = pd.read_csv('examples/dataBar.csv')

fig = plotly_barcharts_3d(df['Gamma'], df['C'], df['score 1'], x_title='Gamma', y_title='C', color='x')
fig.show()
```

![Image medium x](https://github.com/AymericFerreira/Plotly_barchart3D/blob/master/examples/medium_x.png?raw=true)

```
from barchart import plotly_barcharts_3d
import pandas as pd

df = pd.read_csv('examples/dataBar.csv')

fig = plotly_barcharts_3d(df['Gamma'], df['C'], df['score 1'], x_title='Gamma', y_title='C', color='x+y')
fig.show()
```

![Image medium xy](https://github.com/AymericFerreira/Plotly_barchart3D/blob/master/examples/medium_xy.png?raw=true)

Plotly, pandas and numpy needs to be installed and are included in requirements.txt.
```
pip install -r requirements.txt
```
