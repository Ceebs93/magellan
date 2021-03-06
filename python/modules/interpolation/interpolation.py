#!/usr/bin/env python

import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import interp2d


def interpolate_df_cols_2d(df, xcol, ycol, zcol):

    interpolation_func              = interp2d(df[xcol], df[ycol], df[zcol], fill_value=np.inf)
    interpolation_func.bounds_error = False
    
    xmin, xmax = df[xcol].min(), df[xcol].max()
    ymin, ymax = df[ycol].min(), df[ycol].max()
    
    # - Create a dense sample of the interpolated function (for plotting purposes later)
    x_pts = np.linspace(xmin, xmax, num=npts, endpoint=True)
    y_pts = np.linspace(xmin, xmax, num=npts, endpoint=True)
    y_pts = interpolation_func(x_grid)
    z_pts = 0.0
    
    # - Dictionary which is to be stored in 
    interpolation = { 
                          'interpolation_func' : interpolation_func,
                          'x_pts'              : x_pts,
                          'y_pts'              : y_pts,
                          'z_pts'              : z_pts
                        }
    
    return interpolation   



def interpolate_df_cols_1d(df, xcol, ycol, npts=1000):
    """ Create an interpolation from two columns of a pd.DataFrame.
    Returns: A dictionary containing
        - interpoaltion_func: the interpolation function
        - x_pts: grid points along the x axis
        - y pts: interpolated points"""

    interpolation_func              = interp1d(df[xcol], df[ycol], fill_value=np.inf)
    interpolation_func.bounds_error = False
    
    xmin, xmax = df[xcol].min(), df[xcol].max()
    
    # - Create a dense sample of the interpolated function (for plotting purposes later)
    x_pts = np.linspace(xmin, xmax, num=npts, endpoint=True)
    y_pts = interpolation_func(x_grid)
    
    # - Dictionary which is to be stored in 
    interpolation = { 
                          'interpolation_func' : interpolation_func,
                          'x_pts'              : x_pts,
                          'y_pts'              : y_pts
                        }
    
    return interpolation




def create_interpolation_function_df_auto(df,
                                          dependent_variable,
                                          independent_variables,
                                          interp_kwargs={}
                                         ):
    """Creates a 1 or 2d interpolation function from 2 or 3 columns of a pd.DataFrame using
       scipy.interpolate.interp1/2d.
       Arguments: - df: pd.DataFrame storing the array of independent and dependent variables.
                  - dependent_variable: column name of the dependent variable.
                  - independent_variables:  list containing the column name(s) of the independent variable(s).
                  - interp_kwargs: keyword arguments in dictionary format passed onto scipy.interpolate.interp1/2d.
       Returns: The interpolation function"""

    nvars = len(independent_variables)

    if nvars == 1:
        xcol = independent_variables[0]
        ycol = dependent_variable
        interpolation_function = interp1d(df[xcol], df[ycol], fill_value=np.inf, **interp_kwargs)
        interpolation_function.bounds_error = False
    elif nvars == 2:
        xcol = independent_variables[0]
        ycol = independent_variables[1]
        zcol = dependent_variable
        interpolation_function_ = interp2d(df[xcol], df[ycol], df[zcol], fill_value=np.inf, **interp_kwargs)
        def interpolation_function(arg1, arg2, **kwargs):
            val = np.array([interpolation_function_(a1, a2, **kwargs)[0] for a1, a2 in zip(arg1,arg2)] )
            return val
    elif nvars > 2:
        raise Exception('Number of independent variables more than 2! Can only handle 1 or 2 dimensionsal intepolation')
    else:
        raise Exception('Indepdent variables list is empty!')

    return interpolation_function



def create_interpolation_record_df_auto(df,
                                        dependent_variable,
                                        independent_variables,
                                        interp_kwargs={},
                                        npts = 100):
    """Creates a 1 or 2d interpolation function from 2 or 3 columns of a pd.DataFrame using
       scipy.interpolate.interp1/2d, and interpolates along a regular (npts) grid or (npts)*(npts) flattened
       grid along the independent variable(s). Returns a dictionary record containing
       the interpolation function, and the interpolated values along the grid.
       Input: - df: pd.DataFrame storing the array of independent and dependent variables.
              - dependent_variable: column name of the dependent variable.
              - independent_variables:  list containing the column name(s) of the independent variable(s).
              - interp_kwargs: keyword arguments in dictionary format passed onto scipy.interpolate.interp1/2d.
              - npts: number of points along the grid.
       Returns: A dictionary containing the following key value pairs:
                - 'function': interpolation function.
                - 'xpts': grid along the independent variable.
                - 'ypts': grid along the second independent variable (only if len(independent_variables) == 2).
                - 'zpts': interpolated values.
                  """

    interpolation_function = create_interpolation_function_df_auto(df, dependent_variable, independent_variables, interp_kwargs)
    interpolation_function.bounds_error = False
    interpolation = {}
    interpolation["function"] = interpolation_function

    nvars = len(independent_variables)

    if nvars == 1:
        xcol = independent_variables[0]
        xmin, xmax = df[xcol].min(), df[xcol].max()
        xpts = np.linspace(xmin, xmax, num=npts, endpoint=True)
        ypts = interpolation_function(xpts)
        interpolation['xpts'] = xpts
        interpolation['ypts'] = ypts
    elif nvars == 2:
        xcol = independent_variables[0]
        ycol = independent_variables[1]
        xmin, xmax = df[xcol].min(), df[xcol].max()
        ymin, ymax = df[ycol].min(), df[ycol].max()
        xgrid = np.linspace(xmin, xmax, num=npts, endpoint=True)
        ygrid = np.linspace(ymin, ymax, num=npts, endpoint=True)
        X,Y = np.meshgrid(xgrid, ygrid)
        xpts = X.flatten()
        ypts = Y.flatten()
        zpts = interpolation_function(xpts, ypts)
        interpolation['xpts'] = xpts
        interpolation['ypts'] = ypts
        interpolation['zpts'] = zpts
    elif nvars > 2:
        raise Exception('Number of independent variables more than 2! Can only handle 1 or 2 dimensionsal intepolation.')
    else:
        raise Exception('Indepdent variables list is empty!')

    return interpolation
