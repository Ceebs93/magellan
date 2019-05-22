#!/usr/bin/env python

import holoviews as hv
from holoviews import opts
import numpy as np
from plotting.cosmetics import *
#hv.notebook_extension('bokeh')

print('Holoviews version: ', hv.__version__)

#hv.Store.renderers['bokeh'].webgl = True

def load_df(df):

    ds = hv.Dataset(df)
    ds = ds.redim(**hv_v)

    return ds


def mA_dashboard_example(ds):

    cba_tb   = ds.to(hv.Points, kdims=['cba', 'tb'], vdims=[], groupby=['mH_bin']).groupby('mH_bin')

    a = cba_tb

    #cba_tb  = ds.to(hv.Points, kdims=['cba', 'tb'], vdims=[], groupby=['mA_bin']).overlay('k_hdd_type')

    mH_mHc   = a.map(lambda x: x.clone(kdims=[hv_v['mH'], hv_v['mHc']], vdims=[]), [hv.Points])
    xsec_br1 = a.map(lambda x: x.clone(kdims=[hv_v['mA'], hv_v['xsec_sushi_ggh_A_NNLO_x_br_A_Zh']], vdims=[]), [hv.Points])
    xsec_br1 = xsec_br1.redim(xsec_sushi_ggh_A_NNLO_x_br_A_Zh=dict(range=(1e-8,1e2)), mA=dict(range=(1e2,1e3)))

    #ATLAS_CONF_2016_015_AZh_curve.redim(mA=dict(range=(1e2,1e3)))

    xsec_br2 = a.map(lambda x: x.clone(kdims=[hv_v['mA'], hv_v['xsec_sushi_ggh_A_NNLO_x_br_A_tautau']], vdims=[]), [hv.Points])
    xsec_br2 = xsec_br2.redim(xsec_sushi_ggh_A_NNLO_x_br_A_tautau=dict(range=(1e-8,1e1)))
    xsec_br3 = a.map(lambda x: x.clone(kdims=[hv_v['mH'], hv_v['xsec_sushi_ggh_H_NNLO_x_br_H_ZA']], vdims=[]), [hv.Points])
    xsec_br3 = xsec_br3.redim(xsec_sushi_ggh_H_NNLO_x_br_H_ZA=dict(range=(1e-8,1e1)))
    xsec_br4 = a.map(lambda x: x.clone(kdims=[hv_v['mH'], hv_v['xsec_sushi_ggh_H_NNLO_x_br_H_tt']], vdims=[]), [hv.Points])
    xsec_br4 = xsec_br4.redim(xsec_sushi_ggh_H_NNLO_x_br_H_tt=dict(range=(1e-8,1e1)))
    xsec_br5 = a.map(lambda x: x.clone(kdims=[hv_v['mH'], hv_v['xsec_sushi_ggh_H_NNLO_x_br_H_hh']], vdims=[]), [hv.Points])
    xsec_br5 = xsec_br5.redim(xsec_sushi_ggh_H_NNLO_x_br_H_hh=dict(range=(1e-5,1e3)))

    layout = (cba_tb +
              mH_mHc +
              xsec_br1(plot={'Points': {'logx' : False, 'logy': True}}) +
              xsec_br2(plot={'Points': {'logx' : False, 'logy': True}}) +
              xsec_br3(plot={'Points': {'logx' : False, 'logy': True}}) +
              xsec_br4(plot={'Points': {'logx' : False, 'logy': True}}) +
              xsec_br5(plot={'Points': {'logx' : False, 'logy': True}})
             ).cols(2)
    return layout


def create_windows(ds, window_axes=[['cba', 'tb'], ['mH', 'mHc'], ['mA', 'mHc']], doformat=True):

    windows = []
#   window0 = ds.to(hv.Points, kdims=window_axes[0], vdims=[])
    window0 = hv.Points(ds, kdims=[hv_v[window_axes[0][0]], hv_v[window_axes[0][1]]], vdims=[])
#   if doformat:
#       window0 = set_axis_properties(window0)
    windows.append(window0)

    for wax in window_axes[1:]:
        window = window0.map(lambda x: x.clone(kdims=[hv_v[wax[0]], hv_v[wax[1]]], vdims=[]), [hv.Points])
#       if doformat:
#           window = set_axis_properties(window)
        windows.append(window)

    if doformat:
        for window in windows:
           window = set_axis_properties(window)


    return windows

def create_windows_with_groupby(ds, window_axes=[['cba', 'tb'], ['mH', 'mHc'], ['mA', 'mHc']], groupby='mH_bin' ):

    windows = []
    window0 = ds.to(hv.Points, kdims=window_axes[0], vdims=[], groupby=[groupby]).groupby(groupby)
    windows.append(window0)

    for wax in window_axes[1:]:
        window = window0.map(lambda x: x.clone(kdims=[hv_v[wax[0]], hv_v[wax[1]]], vdims=[]), [hv.Points])
        windows.append(window)

    return windows


def concatenate_hmaps(hmaps):

    holomap = item0

    for item in hmaps[1:]:
        holomap += item

    return holomap


def set_axis_properties(holomap):

    xcol = holomap.dimensions()[0].name
    ycol = holomap.dimensions()[1].name

    print(xcol)
    print(ycol)


    opts_dict = {}
    if ycol in log_axes:
        opts_dict['logy'] = True
    if ycol in var_to_limit:
        opts_dict['ylim'] = var_to_limit[ycol]
    if xcol in var_to_limit:
        opts_dict['xlim'] = var_to_limit[xcol]

    holomap = holomap.opts(**opts_dict)
    return holomap



def create_curve_from_measurement(measurement,
                                  observable = "first",
                                  limit_type='limit_exp',
                                  curve_options={'color':'k', 'line_dash':'dashed'}):


    if observable == "first":
        observable = list(measurement.relevant_observables.keys())[0]

    x_grid = measurement['interpolation'][limit_type]['x_grid']
    y_grid = measurement.relevant_observables[observable]["func"](x_grid, limit_type=limit_type)

    data = np.c_[x_grid, y_grid]
    curve = hv.Curve(data).opts(**curve_options)

    return curve
