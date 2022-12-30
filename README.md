![main workflow](https://github.com/aymericFerreira/Plot_barchart3D/actions/workflows/main.yml/badge.svg)
![develop workflow](https://github.com/aymericFerreira/Plot_barchart3D/actions/workflows/main.yml/badge.svg?branch=develop)

# Plotly 3D barchart
Plotly doesn't provide a simple way to create 3D barcharts as matplotlib does.
Here is a function to create them easily via Mesh3D, inspired by *empet* post (https://community.plotly.com/t/how-to-do-a-3d-bar-chart-if-possible/32287/2)

Code is tested for python 3.10 and python 3.11.


## Installation
The only main requirement is plotly. You can install it via pip:
```bash
pip install plotly
```

However, this code is trying to bring more functionalities. To reproduce the examples you will need to install
numpy, pandas and plotly. Pandas package is optional. For reproducibility, the
version used in packages are listed in the requirements.txt file.
```bash
pip install -r requirements.txt
```

Some examples :

Minimal example

```
from barchart import plotly_barcharts_3d
import pandas as pd

xdf = pd.Series([1, 10])
ydf = pd.Series([2, 4])
zdf = pd.Series([10, 30, 20, 45])

fig = plotly_barcharts_3d(xdf, ydf, zdf, color='x+y')
fig.show()
```
![Image small xy](https://github.com/AymericFerreira/Plotly_barchart3D/blob/main/examples/small_xy.png?raw=true)

It can also be used to generate bigger graph and add legends.
```
from barchart import plotly_barcharts_3d
import pandas as pd

df = pd.read_csv('examples/dataBar.csv')

fig = plotly_barcharts_3d(df['Gamma'], df['C'], df['score 1'], x_title='Gamma', y_title='C', color='x')
fig.show()
```

![Image medium x](https://github.com/AymericFerreira/Plotly_barchart3D/blob/main/examples/medium_x.png?raw=true)

```
from barchart import plotly_barcharts_3d
import pandas as pd

df = pd.read_csv('examples/dataBar.csv')

fig = plotly_barcharts_3d(df['Gamma'], df['C'], df['score 1'], x_title='Gamma', y_title='C', color='x+y')
fig.show()
```

![Image medium xy](https://github.com/AymericFerreira/Plotly_barchart3D/blob/main/examples/medium_xy.png?raw=true)

Plotly, pandas and numpy needs to be installed and are included in requirements.txt.
```
pip install -r requirements.txt
```

More documentation about parameters can be found here or in the barchart.py file


**x_df** : Serie of data corresponding to x-axis

**y_df** : Serie of data corresponding to y-axis

**z_df** : Serie of data corresponding to height of the bar chart

**x_min** : Starting position for x-axis

**y_min** : Starting position for y-axis

**z_min** : Minimum value of the barchart, if set to auto minimum value is 0.8 * minimum of z_df to obtain more

packed charts

**step** : Distance between two barcharts

**color** : Axis to create color, possible parameters are

*x* for a different color for each change of x

*y* for a different color for each change of y

or *x+y* to get a different color for each bar

**x_legend** : Legend of x-axis, if set to auto the legend is based on x_df

**y_legend** : Legend of y-axis, if set to auto the legend is based on y_df

**z_legend** : Legend of z-axis, if set to auto the legend is not shown

**flat_shading** :

**x_title** : Title of x-axis

**y_title** : Title of y-axis

**z_title** : Title of z-axis

**hover_info** : Hover info, z by default
