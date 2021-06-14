import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np


def barcharts_from_sparsearray(x_df, y_df, z_df, x_min=0, y_min=0, z_min='auto', step=1, color='x',
                        x_legend='auto', y_legend='auto', z_legend='auto', flat_shading=True,
                        x_title='', y_title='', z_title='', hover_info='z', title=""):
    """
    Convert a dataframe in 3D barcharts similar to matplotlib ones
        Example :
        x_df = pd.Series([1, 1, 10, 10])
        y_df = pd.Series([2, 4, 2 ,4])
        z_df = pd.Series([10, 30, 20, 45])
    :param x_df: Serie or list of data corresponding to x axis
    :param y_df: Serie or list  of data corresponding to y axis
    :param z_df: Serie or list  of data corresponding to height of the bar chart
    :param x_min: Starting position for x axis
    :param y_min: Starting position for y axis
    :param z_min: Minimum value of the barchart, if set to auto minimum value is 0.8 * minimum of z_df to obtain more
    packed charts
    :param step: Distance between two barcharts
    :param color: Axis to create color, possible parameters are
    x for a different color for each change of x
    y for a different color for each change of y
    or x+y to get a different color for each bar
    :param x_legend: Legend of x axis, if set to auto the legend is based on x_df
    :param y_legend: Legend of y axis, if set to auto the legend is based on y_df
    :param z_legend: Legend of z axis, if set to auto the legend is not shown
    :param flat_shading:
    :param x_title: Title of x axis
    :param y_title: Title of y axis
    :param z_title: Title of z axis
    :param hover_info: Hover info, z by default
    :param title: Title of the graph, not functional for the moment
    :return: 3D mesh figure acting as 3D barcharts
    """
    z_df = list(pd.Series(z_df))

    if z_min == 'auto':
        z_min = 0.8 * min(z_df)

    mesh_list = []
    colors = px.colors.qualitative.Plotly
    color_value = 0

    x_df_uniq = np.unique(x_df)
    y_df_uniq = np.unique(y_df)
    len_x_df_uniq = len(x_df_uniq)
    len_y_df_uniq = len(y_df_uniq)

    z_temp_df = []

    if len(z_df) == len_x_df_uniq and len(z_df) == len_y_df_uniq:
        for x in range(len_x_df_uniq):
            for y in range(len_y_df_uniq):
                if x == y:
                    z_temp_df.append(z_df[x])
                else:
                    z_temp_df.append(None)
    z_df = z_temp_df

    for idx, x_data in enumerate(x_df_uniq):
        if color == 'x':
            color_value = colors[idx % 9]

        for idx2, y_data in enumerate(y_df_uniq):
            if color == 'x+y':
                color_value = colors[(idx + idx2 * len(y_df.unique())) % 9]

            elif color == 'y':
                color_value = colors[idx2 % 9]

            x_max = x_min + step
            y_max = y_min + step

            z_max = z_df[idx * len_x_df_uniq + idx2]

            if z_max is not None:

                mesh_list.append(
                    go.Mesh3d(
                        x=[x_min, x_min, x_max, x_max, x_min, x_min, x_max, x_max],
                        y=[y_min, y_max, y_max, y_min, y_min, y_max, y_max, y_min],
                        z=[z_min, z_min, z_min, z_min, z_max, z_max, z_max, z_max],
                        color=color_value,
                        i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                        j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                        k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
                        opacity=1,
                        flatshading=flat_shading,
                        hovertext='text',
                        hoverinfo=hover_info,
                    ))
            else:
                mesh_list.append(
                    go.Mesh3d(
                        x=[x_min, x_min, x_max, x_max, x_min, x_min, x_max, x_max],
                        y=[y_min, y_max, y_max, y_min, y_min, y_max, y_max, y_min],
                        z=[z_min, z_min, z_min, z_min, z_max, z_max, z_max, z_max],
                        color=color_value,
                        i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                        j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                        k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
                        opacity=0.01,
                        flatshading=flat_shading,
                        hovertext='text',
                        hoverinfo=hover_info,
                    ))

            x_min += 2 * step
        y_min += 2 * step
        x_min = 0
    y_min = 0

    if x_legend == 'auto':
        x_legend = x_df_uniq
        x_legend = [str(x_ax) for x_ax in x_legend]
    if y_legend == 'auto':
        y_legend = y_df_uniq
        y_legend = [str(y_ax) for y_ax in y_legend]
    if z_legend == 'auto':
        z_legend = None

    fig = go.Figure(mesh_list)

    fig.update_layout(scene=dict(
        xaxis=dict(
            tickmode='array',
            ticktext=x_legend,
            tickvals=np.arange(x_min, len_x_df_uniq * 2, step=2),
            title=x_title),
        yaxis=dict(
            tickmode='array',
            ticktext=y_legend,
            tickvals=np.arange(y_min, len_y_df_uniq * 2, step=2),
            title=y_title),
        zaxis=dict(title=z_title)))
    if z_legend is None:
        fig.update_layout(scene=dict(
            zaxis=dict(
                tickmode='array',
                ticktext=z_legend,
                title=z_title)),
            template="plotly_white")

    return fig


def barcharts3d_fromarray(x_df, y_df, z_df, x_min=0, y_min=0, z_min='auto', step=1, color='x',
                          x_legend='auto', y_legend='auto', z_legend='auto', flat_shading=True,
                          x_title='', y_title='', z_title='', hover_info='z', title=""):
        """
        Convert a dataframe in 3D barcharts similar to matplotlib ones
            Example :
            x_df = pd.Series([1, 1, 10, 10])
            y_df = pd.Series([2, 4, 2 ,4])
            z_df = pd.Series([10, 30, 20, 45])
        :param x_df: Serie of data corresponding to x axis
        :param y_df: Serie of data corresponding to y axis
        :param z_df: Serie of data corresponding to height of the bar chart
        :param x_min: Starting position for x axis
        :param y_min: Starting position for y axis
        :param z_min: Minimum value of the barchart, if set to auto minimum value is 0.8 * minimum of z_df to obtain more
        packed charts
        :param step: Distance between two barcharts
        :param color: Axis to create color, possible parameters are
        x for a different color for each change of x
        y for a different color for each change of y
        or x+y to get a different color for each bar
        :param x_legend: Legend of x axis, if set to auto the legend is based on x_df
        :param y_legend: Legend of y axis, if set to auto the legend is based on y_df
        :param z_legend: Legend of z axis, if set to auto the legend is not shown
        :param flat_shading:
        :param x_title: Title of x axis
        :param y_title: Title of y axis
        :param z_title: Title of z axis
        :param hover_info: Hover info, z by default
        :param title: Title of the graph, not functional for the moment
        :return: 3D mesh figure acting as 3D barcharts
        """

        if z_min == 'auto':
            z_min = 0.8 * min(z_df)
        mesh_list = []
        colors = px.colors.qualitative.Plotly
        color_value = 0

        x_df_uniq = x_df.unique()
        y_df_uniq = y_df.unique()
        len_x_df_uniq = len(x_df_uniq)
        len_y_df_uniq = len(y_df_uniq)

        for idx, x_data in enumerate(x_df_uniq):
            if color == 'x':
                color_value = colors[idx % 9]
            for idx2, y_data in enumerate(y_df_uniq):
                if color == 'x+y':
                    color_value = colors[(idx + idx2 * len(y_df.unique())) % 9]
                elif color == 'y':
                    color_value = colors[idx2 % 9]
                x_max = x_min + step
                y_max = y_min + step
                z_max = z_df[idx + idx2 * len_x_df_uniq]
                mesh_list.append(
                    go.Mesh3d(
                        x=[x_min, x_min, x_max, x_max, x_min, x_min, x_max, x_max],
                        y=[y_min, y_max, y_max, y_min, y_min, y_max, y_max, y_min],
                        z=[z_min, z_min, z_min, z_min, z_max, z_max, z_max, z_max],
                        color=color_value,
                        i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                        j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                        k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
                        opacity=1,
                        flatshading=flat_shading,
                        hovertext='text',
                        hoverinfo=hover_info,
                    ))
                x_min += 2 * step
            y_min += 2 * step
            x_min = 0
        y_min = 0
        if x_legend == 'auto':
            x_legend = x_df_uniq
            x_legend = [str(x_ax) for x_ax in x_legend]
        if y_legend == 'auto':
            y_legend = y_df_uniq
            y_legend = [str(y_ax) for y_ax in y_legend]
        if z_legend == 'auto':
            z_legend = None

        fig = go.Figure(mesh_list)

        fig.update_layout(scene=dict(
            xaxis=dict(
                tickmode='array',
                ticktext=x_legend,
                tickvals=np.arange(x_min, len_x_df_uniq * 2, step=2),
                title=x_title),
            yaxis=dict(
                tickmode='array',
                ticktext=y_legend,
                tickvals=np.arange(y_min, len_y_df_uniq * 2, step=2),
                title=y_title),
            zaxis=dict(title=z_title)))
        if z_legend is None:
            fig.update_layout(scene=dict(
                zaxis=dict(
                    tickmode='array',
                    ticktext=z_legend,
                    title=z_title)),
                template="plotly_white")

        return fig


def plotly_barcharts_3d(x_df, y_df, z_df, x_min=0, y_min=0, z_min='auto', step=1, color='x',
                        x_legend='auto', y_legend='auto', z_legend='auto', flat_shading=True,
                        x_title='', y_title='', z_title='', hover_info='z', title=""):
    if len(z_df) == (len(x_df) * len(y_df)):
        fig = barcharts3d_fromarray(x_df, y_df, z_df, x_min=x_min, y_min=y_min, z_min=z_min, step=step, color=color,
                                    x_legend=x_legend, y_legend=y_legend, z_legend=z_legend, flat_shading=flat_shading,
                                    x_title=x_title, y_title=y_title, z_title=z_title, hover_info=hover_info)
    else:
        fig = barcharts_from_sparsearray(x_df, y_df, z_df, x_min=x_min, y_min=y_min, z_min=z_min, step=step,
                                         color=color, x_legend=x_legend, y_legend=y_legend, z_legend=z_legend,
                                         flat_shading=flat_shading, x_title=x_title, y_title=y_title, z_title=z_title,
                                         hover_info=hover_info)
    return fig


if __name__ == '__main__':
    features = [2, 3, 5, 10, 20]
    neighbours = [31, 24, 10, 28, 48]
    accuracies = [0.9727, 0.9994, 0.9994, 0.9995, 0.9995]
    plotly_barcharts_3d(features, neighbours, accuracies,
                        x_title="Features", y_title="Neighbours", z_title="Accuracy").show()
    xdf = pd.Series([1, 10])
    ydf = pd.Series([2, 4])
    zdf = pd.Series([10, 30, 20, 45])
    fig = plotly_barcharts_3d(xdf, ydf, zdf, color='x+y')
    fig.show()
