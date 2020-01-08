from typing import Tuple

import numpy as np
import plotly.offline as py
import plotly.graph_objs as go

def graph_x(val: int = 20):
    x = np.linspace(-0.5 * val, 1.5 * val, num=200)
    y = np.power(x, 1)

    data = [go.Scatter(x=x, y=y)]

    layout = go.Layout(
        title="Graph of f(x) = x",
        autosize=True,
        margin=dict(l=65, r=50,
                    b=65, t=90,)
    )

    return py.iplot(go.Figure(data=data, layout=layout))

def graph_x2(val: int = 10):
    x = np.linspace(-1. * val, 1. * val, num=200)
    y = np.power(x, 2) - x + 4

    data = [go.Scatter(x=x, y=y)]

    layout = go.Layout(
        title="Graph of f(x) = x^2 - x + 4",
        autosize=True,
        margin=dict(l=65, r=50,
                    b=65, t=90,)
    )

    return py.iplot(go.Figure(data=data, layout=layout))

def graph_chain(val: int = 10):
    x = np.linspace(-1. * val, 1. * val, num=200)
    y = np.power(3 * np.power(x, 2) + x - 4, 3)

    data = [go.Scatter(x=x, y=y)]

    layout = go.Layout(
        title="Graph of f(x) = (3x^2 + x - 4)^3",
        autosize=True,
        margin=dict(l=65, r=50,
                    b=65, t=90,)
    )

    return py.iplot(go.Figure(data=data, layout=layout))

def graph_saddle(val: int = 10):
    x = np.linspace(-1. * val, 1. * val, num=200)
    y = np.linspace(-1. * val, 1. * val, num=200)
    y_grid, x_grid = np.meshgrid(x, y)
    z = (y_grid * np.power(x_grid, 2)) - 3 * np.power(y_grid, 2)

    data = [go.Surface(x=x, y=y, z=z, colorscale="Blues", showscale=False)]

    layout = go.Layout(
        title="Graph of f(x, y) = yx^2 - 3y^2",
        autosize=True,
        margin=dict(l=65, r=50,
                    b=65, t=90,)
    )

    return py.iplot(go.Figure(data=data, layout=layout))

def graph_simpler_3d(x: int, y: int, val: int = 10):
    x_lin = np.linspace(-1. * val, 1. * val, num=200)
    y_lin = np.linspace(-1. * val, 1. * val, num=200)
    y_grid, x_grid = np.meshgrid(x_lin, y_lin)
    
    def get_z(x, y):
        return np.power(x, 2) - 3 * np.power(y, 2)
    
    z_lin = get_z(x_grid, y_grid)
    
    x1 = np.array([x])
    y1 = np.array([y])
    z1 = get_z(x1, y1)

    data = [go.Surface(x=x_lin, y=y_lin, z=z_lin, colorscale="Blues", showscale=False),
            go.Scatter3d(x=x1, y=y1, z=z1, mode="markers", hovertext=["Intersection"]),]

    layout = go.Layout(
        title="Graph of f(x, y) = x^2 - 3y^2",
        autosize=True,
        margin=dict(l=65, r=50,
                    b=65, t=90,)
    )

    return py.iplot(go.Figure(data=data, layout=layout))

def graph_x_y_projection(x: int, y: int, val: int = 10):
    x_lin = np.linspace(-1. * val, 1. * val, num=200)
    y_lin = np.linspace(-1. * val, 1. * val, num=200)
    y_grid, x_grid = np.meshgrid(x_lin, y_lin)
    
    def get_z(x, y):
        return np.power(x, 2) - 3 * np.power(y, 2)
    
    z_lin = get_z(x_grid, y_grid)
    
    x1 = np.array([x])
    y1 = np.array([y])
    z1 = get_z(x1, y1)

    # ordering to preserve color
    data = [go.Surface(x=x_lin, y=np.full_like(y_grid, y), z=z_lin, colorscale="Blues", showscale=False),
            go.Scatter3d(x=x1, y=y1, z=z1, mode="markers", hovertext=["Intersection"]),
            go.Surface(x=np.full_like(x_grid, x), y=y_lin, z=z_lin, colorscale="Blues", showscale=False),]

    layout = go.Layout(
        title="Graph of f(x, y) = x^2 - 3y^2",
        autosize=True,
        margin=dict(l=65, r=50,
                    b=65, t=90,)
    )    

    return py.iplot(go.Figure(data=data, layout=layout))