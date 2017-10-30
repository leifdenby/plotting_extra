# coding: utf-8
"""
Utilities for creating specialised plots
"""

import numpy as np
import matplotlib.pyplot as plot

def oneway_normed_hist2d(x, y, axis, dxdy=None, range=None):
    """
    2D histogram which is normed in bins along axis defined by `axis`

    NB: `range` is truncated to resolution in `dxdy` if provided
    """
    p_axis = (axis + 1) % 2

    if dxdy is not None:
        dx, dy = dxdy
        if range is not None:
            (_x_min, _x_max), (_y_min, _y_max) = range
        else:
            _x_min, _x_max = x.min(), x.max()
            _y_min, _y_max = y.min(), y.max()

        x_min = dx*int(_x_min/dx)
        x_max = dx*int(_x_max/dx)
        y_min = dy*int(_y_min/dy)
        y_max = dy*int(_y_max/dy)

        range = ((x_min, x_max), (y_min, y_max))

        lx = x_max - x_min
        ly = y_max - y_min

        nx = int(lx/dx)
        ny = int(ly/dy)

        bins = np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny)

        if nx == 1 or ny == 1:
            raise Exception("Bin width too small in x or y direction")
    else:
        if range is None:
            range = ((x.min(), x.max()), (y.min(), y.max()))
        bins = 30, 20

    H, xedges, yedges = np.histogram2d(x, y, bins=bins, range=range)

    nx, ny = H.shape

    H_sum_x = np.sum(H, axis=axis)
    assert H_sum_x.shape[0] == H.shape[p_axis]
    fn_rot = lambda v: [v, v.T][p_axis]
    h = H/fn_rot(np.outer(H_sum_x, np.ones((H.shape[axis],))))
    x, y = np.meshgrid(xedges, yedges, indexing='ij')

    plot.pcolormesh(x, y, h)
