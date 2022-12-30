from __future__ import annotations

import pathlib

import numpy as np
import pandas as pd
import pytest

from barchart import plotly_bar_charts_3d
from barchart import verify_input


def test_array_from_barchart():
    features = [2, 3, 5, 10, 20]
    neighbours = [31, 24, 10, 28, 48]
    accuracies = [0.9727, 0.9994, 0.9994, 0.9995, 0.9995]
    fig = plotly_bar_charts_3d(
        features, neighbours, accuracies,
        x_title='Features', y_title='Neighbours', z_title='Accuracy',
    ).__str__()
    truth = pathlib.Path('tests/truth_array_from_barchart.txt').read_text()
    assert (fig.__str__() == truth)

    features2 = pd.Series([2, 3, 5, 10, 20])
    neighbours2 = pd.Series([31, 24, 10, 28, 48])
    accuracies2 = pd.Series([0.9727, 0.9994, 0.9994, 0.9995, 0.9995])
    fig2 = plotly_bar_charts_3d(
        features2, neighbours2, accuracies2,
        x_title='Features', y_title='Neighbours', z_title='Accuracy',
    ).__str__()

    assert (fig.__str__() == fig2.__str__())


def test_array_from_barchart_not_unique():
    features = [2, 2, 4, 4, 20]
    neighbours = [31, 24, 31, 28, 24]
    accuracies = [0.9727, 0.9994, 0.9994, 0.9995, 0.9995]
    fig = plotly_bar_charts_3d(
        features, neighbours, accuracies,
        x_title='Features', y_title='Neighbours', z_title='Accuracy',
    )
    assert (
        fig.__str__() == """Figure({
    'data': [{'color': '#636EFA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 1,
              'type': 'mesh3d',
              'x': [0, 0, 1, 1, 0, 0, 1, 1],
              'y': [0, 1, 1, 0, 0, 1, 1, 0],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, 0.9727, 0.9727, 0.9727, 0.9727]},
             {'color': '#636EFA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [2, 2, 3, 3, 2, 2, 3, 3],
              'y': [0, 1, 1, 0, 0, 1, 1, 0],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#636EFA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [4, 4, 5, 5, 4, 4, 5, 5],
              'y': [0, 1, 1, 0, 0, 1, 1, 0],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#636EFA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [6, 6, 7, 7, 6, 6, 7, 7],
              'y': [0, 1, 1, 0, 0, 1, 1, 0],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#636EFA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [8, 8, 9, 9, 8, 8, 9, 9],
              'y': [0, 1, 1, 0, 0, 1, 1, 0],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#EF553B',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [0, 0, 1, 1, 0, 0, 1, 1],
              'y': [2, 3, 3, 2, 2, 3, 3, 2],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#EF553B',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 1,
              'type': 'mesh3d',
              'x': [2, 2, 3, 3, 2, 2, 3, 3],
              'y': [2, 3, 3, 2, 2, 3, 3, 2],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, 0.9994, 0.9994, 0.9994, 0.9994]},
             {'color': '#EF553B',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [4, 4, 5, 5, 4, 4, 5, 5],
              'y': [2, 3, 3, 2, 2, 3, 3, 2],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#EF553B',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [6, 6, 7, 7, 6, 6, 7, 7],
              'y': [2, 3, 3, 2, 2, 3, 3, 2],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#EF553B',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [8, 8, 9, 9, 8, 8, 9, 9],
              'y': [2, 3, 3, 2, 2, 3, 3, 2],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#00CC96',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [0, 0, 1, 1, 0, 0, 1, 1],
              'y': [4, 5, 5, 4, 4, 5, 5, 4],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#00CC96',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [2, 2, 3, 3, 2, 2, 3, 3],
              'y': [4, 5, 5, 4, 4, 5, 5, 4],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#00CC96',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 1,
              'type': 'mesh3d',
              'x': [4, 4, 5, 5, 4, 4, 5, 5],
              'y': [4, 5, 5, 4, 4, 5, 5, 4],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, 0.9994, 0.9994, 0.9994, 0.9994]},
             {'color': '#00CC96',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [6, 6, 7, 7, 6, 6, 7, 7],
              'y': [4, 5, 5, 4, 4, 5, 5, 4],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#00CC96',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [8, 8, 9, 9, 8, 8, 9, 9],
              'y': [4, 5, 5, 4, 4, 5, 5, 4],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#AB63FA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [0, 0, 1, 1, 0, 0, 1, 1],
              'y': [6, 7, 7, 6, 6, 7, 7, 6],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#AB63FA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [2, 2, 3, 3, 2, 2, 3, 3],
              'y': [6, 7, 7, 6, 6, 7, 7, 6],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#AB63FA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [4, 4, 5, 5, 4, 4, 5, 5],
              'y': [6, 7, 7, 6, 6, 7, 7, 6],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#AB63FA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 1,
              'type': 'mesh3d',
              'x': [6, 6, 7, 7, 6, 6, 7, 7],
              'y': [6, 7, 7, 6, 6, 7, 7, 6],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, 0.9995, 0.9995, 0.9995, 0.9995]},
             {'color': '#AB63FA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [8, 8, 9, 9, 8, 8, 9, 9],
              'y': [6, 7, 7, 6, 6, 7, 7, 6],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#FFA15A',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [0, 0, 1, 1, 0, 0, 1, 1],
              'y': [8, 9, 9, 8, 8, 9, 9, 8],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#FFA15A',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [2, 2, 3, 3, 2, 2, 3, 3],
              'y': [8, 9, 9, 8, 8, 9, 9, 8],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#FFA15A',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [4, 4, 5, 5, 4, 4, 5, 5],
              'y': [8, 9, 9, 8, 8, 9, 9, 8],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#FFA15A',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 0.01,
              'type': 'mesh3d',
              'x': [6, 6, 7, 7, 6, 6, 7, 7],
              'y': [8, 9, 9, 8, 8, 9, 9, 8],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, None, None, None, None]},
             {'color': '#FFA15A',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 1,
              'type': 'mesh3d',
              'x': [8, 8, 9, 9, 8, 8, 9, 9],
              'y': [8, 9, 9, 8, 8, 9, 9, 8],
              'z': [0.7781600000000001, 0.7781600000000001, 0.7781600000000001,
                    0.7781600000000001, 0.9995, 0.9995, 0.9995, 0.9995]}],
    'layout': {'scene': {'xaxis': {'tickmode': 'array',
                                   'ticktext': [2, 2, 4, 4, 20],
                                   'tickvals': array([0, 2, 4, 6, 8]),
                                   'title': {'text': 'Features'}},
                         'yaxis': {'tickmode': 'array',
                                   'ticktext': [31, 24, 31, 28, 24],
                                   'tickvals': array([0, 2, 4, 6, 8]),
                                   'title': {'text': 'Neighbours'}},
                         'zaxis': {'tickmode': 'array', 'title': {'text': 'Accuracy'}}},
               'template': '...',
               'title': {'text': ''}}
})"""
    )

    features2 = pd.Series([2, 2, 4, 4, 20])
    neighbours2 = pd.Series([31, 24, 31, 28, 24])
    accuracies2 = pd.Series([0.9727, 0.9994, 0.9994, 0.9995, 0.9995])
    fig2 = plotly_bar_charts_3d(
        features2, neighbours2, accuracies2,
        x_title='Features', y_title='Neighbours', z_title='Accuracy',
    ).__str__()

    assert (fig.__str__() == fig2.__str__())


def test_sparse_from_barchart():
    xdf = [1, 10]
    ydf = [2, 4]
    zdf = [10, 30, 20, 45]
    fig = plotly_bar_charts_3d(xdf, ydf, zdf, color='x+y')

    assert (
        fig.__str__() == """Figure({
    'data': [{'color': '#636EFA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 1,
              'type': 'mesh3d',
              'x': [0, 0, 1, 1, 0, 0, 1, 1],
              'y': [0, 1, 1, 0, 0, 1, 1, 0],
              'z': [8.0, 8.0, 8.0, 8.0, 10, 10, 10, 10]},
             {'color': '#00CC96',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 1,
              'type': 'mesh3d',
              'x': [2, 2, 3, 3, 2, 2, 3, 3],
              'y': [0, 1, 1, 0, 0, 1, 1, 0],
              'z': [8.0, 8.0, 8.0, 8.0, 20, 20, 20, 20]},
             {'color': '#EF553B',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 1,
              'type': 'mesh3d',
              'x': [0, 0, 1, 1, 0, 0, 1, 1],
              'y': [2, 3, 3, 2, 2, 3, 3, 2],
              'z': [8.0, 8.0, 8.0, 8.0, 30, 30, 30, 30]},
             {'color': '#AB63FA',
              'flatshading': True,
              'hoverinfo': 'z',
              'hovertext': 'text',
              'i': [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
              'j': [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
              'k': [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
              'opacity': 1,
              'type': 'mesh3d',
              'x': [2, 2, 3, 3, 2, 2, 3, 3],
              'y': [2, 3, 3, 2, 2, 3, 3, 2],
              'z': [8.0, 8.0, 8.0, 8.0, 45, 45, 45, 45]}],
    'layout': {'scene': {'xaxis': {'tickmode': 'array',
                                   'ticktext': [1, 10],
                                   'tickvals': array([0, 2]),
                                   'title': {'text': ''}},
                         'yaxis': {'tickmode': 'array',
                                   'ticktext': [2, 4],
                                   'tickvals': array([0, 2]),
                                   'title': {'text': ''}},
                         'zaxis': {'tickmode': 'array', 'title': {'text': ''}}},
               'template': '...',
               'title': {'text': ''}}
})"""
    )

    xdf2 = pd.Series([1, 10])
    ydf2 = pd.Series([2, 4])
    zdf2 = pd.Series([10, 30, 20, 45])
    fig2 = plotly_bar_charts_3d(xdf2, ydf2, zdf2, color='x+y')

    assert (fig.__str__() == fig2.__str__())


def test_sparse_from_barchart_not_unique():
    xdf = [1, 1]
    ydf = [2, 2]
    zdf = [10, 30, 20, 20]
    fig = plotly_bar_charts_3d(xdf, ydf, zdf, color='x+y')
    truth = pathlib.Path(
        'tests/truth_sparse_from_barchart_not_unique.txt',
    ).read_text()

    assert (
        fig.__str__() == truth
    )

    xdf2 = pd.Series([1, 1])
    ydf2 = pd.Series([2, 2])
    zdf2 = pd.Series([10, 30, 20, 20])
    fig2 = plotly_bar_charts_3d(xdf2, ydf2, zdf2, color='x+y')

    assert (fig.__str__() == fig2.__str__())


def test_verify_input():
    features = [2, 3, 5, 10, 20]
    neighbours = [31, 24, 10, 28, 48]
    accuracies = [0.9727, 0.9994, 0.9994, 0.9995, 0.9995]
    assert verify_input(features, neighbours, accuracies) is True
    xdf = pd.Series([1, 10])
    ydf = pd.Series([2, 4])
    zdf = pd.Series([10, 30, 20, 45])
    assert verify_input(xdf, ydf, zdf) is True
    with pytest.raises(ValueError, match='Input arguments are not matching.'):
        verify_input(
            np.random.random(
                10,
            ), np.random.random(7), np.random.random(11),
        )
