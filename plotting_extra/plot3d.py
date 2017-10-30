# coding: utf-8
"""
Utilities for creating specialised plots in 3D
"""

from skimage import measure
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def isosurface_3d_marching_cubes(x, y, z, v, v_surface, spacing):
    """
    Plot isosurface using marching cubes to create triangulated surface and
    plot as wireframe

    Inspired from https://stackoverflow.com/a/35472146
    """
    if type(spacing) == float:
        spacing = (spacing, spacing, spacing)
    verts, faces, _, _ = measure.marching_cubes_lewiner(
        v, v_surface, spacing=spacing)

    fig = plot.gcf()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0] + x.min(), verts[:,1] + y.min(), faces,
            verts[:, 2] + z.min(), cmap='Spectral', lw=1)


    max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0

    mid_x = (x.max()+x.min()) * 0.5
    mid_y = (y.max()+y.min()) * 0.5
    mid_z = (z.max()+z.min()) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    return ax
