#!/usr/bin/env python

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.colors as mcolors
import matplotlib_utils.plot_func as mpl_utils

import analysis.analysis as analysis
from plotting.cosmetics import *


##################################
#####                        #####
##### ----- Prototypes ----- #####
#####                        #####
##################################
"""These are atomic plotting functions reused in other functions."""


def scatter(df, xcol, ycol,
        ax=None, scatter_kwargs={'color':"C0", "rasterized":True}, auto_axis_limits=True):
    """Scatter plot of df[xcol] and df[ycol] with a single color and automatic latex axis labels and ranges.
    If ax=None is then create a new subplot.
    Returns: fig, ax"""

    if ax is None:
        fig,ax = plt.subplots()
    else:
        fig = None

    ax.scatter(df[xcol], df[ycol], **scatter_kwargs)

    xlabel = var_to_label[xcol]
    ylabel = var_to_label[ycol]

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if auto_axis_limits:
        ax = set_axis_limits(ax)

    return fig,ax


def scatter_windows(df, window_axes,
                    ax=None,
                    ncols=3,
                    scatter_kwargs={"rasterized":True}):
    """Scatter plot of multiple windows.
       - window_axes is a list containing tuples of xcol and ycol.
         E.g. window_axes = [('cba', 'tb), ('mA', 'mH')]
         Returns: fig, ax."""

    nwindows = len(window_axes)
    nrows = int(nwindows/ncols + 0.5)

    if ax is None:
        fig,axes = plt.subplots(nrows=nrows, ncols=ncols)
        ax = axes.flatten()
    else:
        fig = None

    for i, wax in enumerate(window_axes):
        scatter(df, wax[0], wax[1], ax[i], scatter_kwargs=scatter_kwargs)

    return fig, ax


def scatter_color(df, xcol, ycol, zcol, order=True, cmap='jet', fig=None, ax=None, scatter_kwargs={}):

    if ax is None:
        fig,ax = plt.subplots()

    sorted = df.sort_values(by=[zcol], ascending=[order])
    sorted.plot.scatter(x=xcol, y=ycol, c=zcol, colormap=cmap, alpha=1.0, ax=ax, **scatter_kwargs)

    cax = fig.get_axes()[1]
    
    # - Labels
    xlabel = var_to_label[xcol]
    ylabel = var_to_label[ycol]
    zlabel = var_to_label[zcol]

    ax.set_xlabel(xlabel);
    ax.set_ylabel(ylabel);
    cax.set_ylabel(zlabel)

    return fig, ax


#######################################################################################################
######################################################
#####                                            #####
##### ----- Specialised plotting functions ----- #####
#####                                            #####
######################################################

def scatter_alignment_wrong_sign(df, xcol, ycol,
                                 ax=None, wrong_sign_alpha=0.7,
                                alignment_alpha=0.05, scatter_kwargs={}):
    """Scatter plot of df[xcol] and df[ycol] separately showing the alignment and wrong sign."""

    if ax is None:
        fig,ax = plt.subplots()

    wrong_sign = df.query('k_hdd < 0.0')
    alignment  = df.query('k_hdd > 0.0')

    if len(alignment) != 0:
        alignment.plot.scatter (xcol, ycol, c=cat_to_color['alignment'],  alpha=alignment_alpha,
                ax=ax, **scatter_kwargs)
    if len(wrong_sign) != 0:
        wrong_sign.plot.scatter(xcol, ycol, c=cat_to_color['wrong_sign'], alpha=wrong_sign_alpha,
                ax=ax, **scatter_kwargs)

    xlabel = var_to_label[xcol]
    ylabel = var_to_label[ycol]

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    return fig, ax


##################################################################
#########################
### --- Exclusions--- ###
#########################

def exclusion_from_analysis(df, measurement, window_axes, observable='first',
        limit_type='limit_exp', limit_scaling_factor=1.0, ncols=3, scatter_kwargs={'rasterized':True},
        plot_order='excl_nonexcl'):

    print("exclusion_from_analysis() started")
    print("limit_scaling_factor: {}".format(limit_scaling_factor))

    nwindows = len(window_axes)
    nrows = int(nwindows/ncols + 0.5)

    if observable == 'first':
        observable = list(measurement.observables.keys())[0]

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols)
    ax = axes.flatten()

    all_pts = df
    print("Determining excluded points.")
    idx_excl_pts     = measurement.get_idx_of_excluded_pts(df, observable=observable,
            limit_type=limit_type, limit_scaling_factor=limit_scaling_factor)
    idx_not_excl_pts = ~idx_excl_pts
    excl_pts     = df[idx_excl_pts]
    not_excl_pts = df[idx_not_excl_pts]
    print("Got excluded and non-excluded points.")

    for i, wax in enumerate(window_axes):

        label_excl     = "Excluded by the analysis".format(measurement['label']) 
        label_not_excl = "Not excluded".format(measurement['label']) 
#       if scale != 1.0:
#           label_excl     += "limit scale ".format(measurement['label']) 
#           label_not_excl += "limit scale ".format(measurement['label']) 

        if plot_order == 'excl_nonexcl':
            scatter_kwargs.update({'label':label_excl})
            scatter_kwargs.update({'color':'firebrick'})
            scatter(excl_pts,      wax[0], wax[1], ax[i], scatter_kwargs=scatter_kwargs)
    
            scatter_kwargs.update({'label':label_not_excl})
            scatter_kwargs.update({'color':'navy'})
            scatter(not_excl_pts,  wax[0], wax[1], ax[i], scatter_kwargs=scatter_kwargs)
        elif plot_order == 'nonexcl_excl':
            scatter_kwargs.update({'label':label_not_excl})
            scatter_kwargs.update({'color':'navy'})
            scatter(not_excl_pts,  wax[0], wax[1], ax[i], scatter_kwargs=scatter_kwargs)

            scatter_kwargs.update({'label':label_excl})
            scatter_kwargs.update({'color':'firebrick'})
            scatter(excl_pts,      wax[0], wax[1], ax[i], scatter_kwargs=scatter_kwargs)

    print("Scatter plots finished.")
    # - First axis measurement limit
    xvar = window_axes[0][0]
    yvar = window_axes[0][1]
    xmin, xmax, ngridpts = df[xvar].min(), df[xvar].max(), 100
    xi = np.linspace(xmin, xmax, ngridpts)

#   if len(measurement.observables[observable]["upper_limit"]['arguments']) == 2:
#       yi = measurement.observables[observable]["upper_limit"]['function'](np.c_[[xi, np.zeros_like(xi)]], limit_type)
#   elif len(measurement.observables[observable]["upper_limit"]['arguments']) == 1:
#       yi = measurement.observables[observable]["upper_limit"]['function'](xi, limit_type)
#   else:
#       pass

    if len(measurement.observables[observable]["upper_limit"]['arguments']) == 1:
        yi = measurement.observables[observable]["upper_limit"]['function'](xi, limit_type)

        label_limit_curve = "{} {}".format(measurement['label'], var_to_label[limit_type])
        if limit_scaling_factor != 1.0:
            label_limit_curve += " scaled".format(limit_scaling_factor)
        ax[0].plot(xi, scale*yi, linestyle='--', c='k', label=label_limit_curve)
        print("Limit curve finished")

    #naxes = len(ax)
    #fig.delaxes(ax[])

    return fig, ax


def exclusion_from_analysis_projection(df, window_axes, measurement, observable='first',
        plot_order='excl_nonexcl', lumiscale=1.0, ncols=3):

    limit_scaling_factor = 1.0/np.sqrt(lumiscale)
    
    if observable == 'first':
        observable = list(measurement.observables.keys())[0]
    
    fig, ax = exclusion_from_analysis(df, measurement=measurement,
            window_axes=window_axes, observable=observable, plot_order=plot_order,
            limit_scaling_factor=limit_scaling_factor, ncols=ncols)

    print("Finished with exclusion_from_analysis() function.")
    
    ax[0].set_yscale('log')
    ax[0].set_ylim(1e-3,12)
    
    title  = r"Naive projection of exclusion based on {} ({})".format(measurement['process'], measurement['label'])
    title += "\n"
    title += r"$\mathcal{L}^{\mathrm{current}}_{\mathrm{int}}$"
    title += r"= {:.1f} fb$^{{-1}}$, ".format(measurement['luminosity'])
    title += r"$\mathcal{L}_{\mathrm{int}}^{\mathrm{future}}=$"
    title += " {:.1f} fb$^{{-1}}$".format(measurement['luminosity']*lumiscale)
    title += " (limit scaled by {:.2f})".format(limit_scaling_factor)
    fig.suptitle(title)
    plt.subplots_adjust(top=0.90)
    
    ax[0].legend()
    return fig, ax


def exclusion_exp_and_theory_cba_tanb_plane(df, mA, mH, mHc, Z7, chi2_col=False, chi2_bounds=[],
        HiggsBounds=False,
        theory_constraints=['per_8pi', 'uni', 'sta'], fig=None, ax=None
        ):

    query_str = "mA == {} & mH == {} & Z7 == {}".format(mA, mH, Z7)
    dfr = df.query(query_str)

    text_mH  = r"$m_{{H}} = {}$ GeV".format(mH)
    text_mHc = r"$m_{{H^{{\pm}}}} = {}$ GeV".format(mHc)
    text_mA  = r"$m_{{A}} = {}$ GeV".format(mA)
    text_Z7  = r"$Z_{{7}} = {}$".format(Z7)
    sidebox_text = [text_mH, text_mHc, text_mA, text_Z7]
    sidebox_legends = list(theory_constraints)

    if chi2_col:
        sidebox_legends.append('sigma1')
        sidebox_legends.append('sigma2')
        sidebox_legends.append('sigma3')

    if HiggsBounds:
        sidebox_legends.append('HiggsBounds') 

    fig,ax = exclusion_exp_and_theory(dfr, xcol='cba', ycol='tb',
                        chi2_col=chi2_col, chi2_bounds=chi2_bounds, HiggsBounds=HiggsBounds,
                        theory_constraints=theory_constraints, fig=None, ax=None,
#                       sidebox_text=sidebox_text, sidebox_legends=sidebox_legends)
                        sidebox_text=[], sidebox_legends=[])


    return fig,ax


def exclusion_exp_and_theory(df, xcol, ycol, chi2_col=False, chi2_bounds=[], HiggsBounds=False, 
        theory_constraints=['per_8pi', 'uni', 'sta'],fig=None, ax=None, sidebox_text=[],
        sidebox_legends=[]):

    ax_sidebox = False

    default_fig_width, default_fig_height = 10, 7
    fig = plt.figure(figsize=(default_fig_width, default_fig_height))
    fig,ax = plt.subplots()


    if ax is None:
        default_fig_width, default_fig_height = plt.rcParams['figure.figsize']
#       if sidebox_text or sidebox_legends:
        if False:
            fig = plt.figure(figsize=(default_fig_width*1.3, default_fig_height))
            ax_sidebox = fig.add_axes([0.0, 0.05, 0.24, 0.9])
            ax_sidebox.grid('off')
            #ax_sidebox.axis('off')
            ax_sidebox.set_xticks(())
            ax_sidebox.set_yticks(())
            ax = fig.add_axes([0.32, 0.05, 0.65, 0.9])
#       else:
#           fig = plt.figure(figsize=(default_fig_width, default_fig_height))
            #ig,ax = plt.subplots()


    if chi2_col:
        chi2_levels(df, xcol, ycol, chi2_col, chi2_bounds, fig=fig, ax=ax)

    if HiggsBounds:
        HiggsBounds_exclusion(df, xcol, ycol, fig=fig, ax=ax)

    if theory_constraints:
        theory_exclusion(df, xcol, ycol, theory_constraints=theory_constraints, fig=fig, ax=ax)

#   if sidebox_text or sidebox_legends:
#       fig.subplots_adjust(left=0.5)

#       print("Creating sidebox")
#       text_xpos = 0.02
#       text_ypos_start = 0.90
#       text_vspace = 0.07
#   
#       for i,text in enumerate(sidebox_text):
#           fig.text(text_xpos, text_ypos_start-i*text_vspace, text, transform=ax.transAxes, fontsize=18)


#       for legend in sidebox_legends:
#   
#           color      = var_to_color[legend]
#           marker     = var_to_marker[legend]
#           markersize = var_to_markersize.get(legend)
#           linewidth  = var_to_linewidth[legend]
#           facecolor  = var_to_facecolor.get(legend, color)
#           edgecolor  = var_to_edgecolor.get(legend, color)
#           alpha      = var_to_alpha[legend]
#   
#           legend_label = var_to_label[legend]
#           ax_sidebox.scatter(-1, -1, marker=marker, s=markersize, linewidth=linewidth, edgecolor=edgecolor,
#                    facecolor=facecolor, label=legend_label)
#   
#       ax_sidebox.set_xlim(0.0, 1.0)
#       ax_sidebox.legend(loc=(-0.02, 0.2), frameon=False, fontsize=15, labelspacing=1)

    if ax_sidebox:
        return fig,ax,ax_sidebox
    else:
        return fig,ax


def plot_projection(df1, df2, planes,
                    colors=('navy', 'firebrick'), labels=('group1', 'group2'), alphas=(1.0, 1.0),
                    scatter_kwargs={}):

    fig, ax = plt.subplots(ncols=2, nrows=3)
    ax = ax.flatten()

    for i, (x, y) in enumerate(planes):

        if i == 0:
            df1.plot.scatter(x, y, ax=ax[i], alpha=alphas[0], color=colors[0],
                    label=labels[0], **scatter_kwargs)
            df2.plot.scatter(x, y, ax=ax[i], alpha=alphas[1], color=colors[1],
                    label=labels[1], **scatter_kwargs)
        else:
            df1.plot.scatter(x, y, ax=ax[i], alpha=alphas[0], color=colors[0], **scatter_kwargs)
            df2.plot.scatter(x, y, ax=ax[i], alpha=alphas[1], color=colors[1], **scatter_kwargs)


        ax[i].set_xlabel(var_to_label[x])
        ax[i].set_ylabel(var_to_label[y])

    return fig, ax


def HiggsBounds_exclusion(df, xcol, ycol, fig=None, ax=None):

    if ax is None:
        fig,ax = plt.subplots()

    query_str = "tot_hbobs > 1.0"
    exclusion_by_HiggsBounds = df.query(query_str) 

    color = var_to_color['HiggsBounds']
    marker = var_to_marker['HiggsBounds']
    markersize = var_to_markersize['HiggsBounds']
    linewidth  = var_to_linewidth['HiggsBounds']
    facecolor  = var_to_facecolor.get('HiggsBounds', color)
    edgecolor  = var_to_edgecolor.get('HiggsBounds', color)
    alpha      = var_to_alpha['HiggsBounds']

    exclusion_by_HiggsBounds.plot.scatter(xcol, ycol, c=color, marker=marker,
            s=markersize, linewidth=linewidth, facecolor=facecolor, edgecolor=edgecolor,
            alpha=alpha, ax=ax)

    xlabel = var_to_label[xcol]
    ylabel = var_to_label[ycol]

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    return fig,ax


def theory_exclusion(df, xcol, ycol, theory_constraints=['per_8pi', 'uni', 'sta'], fig=None, ax=None):

    if ax is None:
        fig,ax = plt.subplots()


    exclusions_by_theory_constraints = []

    for theory_constraint in theory_constraints:
        condition = '{} == 0'.format(theory_constraint)
        exclusion_by_theory_constraint = df.query(condition) 

        color = var_to_color[theory_constraint]
        marker = var_to_marker[theory_constraint]
        markersize = var_to_markersize[theory_constraint]
        linewidth  = var_to_linewidth[theory_constraint]
        facecolor  = var_to_facecolor.get(theory_constraint, color)
        edgecolor  = var_to_edgecolor.get(theory_constraint, color)
        alpha      = var_to_alpha[theory_constraint]


        exclusion_by_theory_constraint.plot.scatter(xcol, ycol, c=color, marker=marker,
                s=markersize, linewidth=linewidth, facecolor=facecolor, edgecolor=edgecolor,
                alpha=alpha, ax=ax)
        exclusions_by_theory_constraints.append(exclusion_by_theory_constraint)

    xlabel = var_to_label[xcol]
    ylabel = var_to_label[ycol]

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    return fig,ax


##################################################################################
#################################
### --- Model exploration --- ###
#################################

def scatter_channel_brs(df, xcol, ycol, channels, fig=None, ax=None, scatter_kwargs={}):

    if ax is None:
        fig,ax = plt.subplots()

    for ch, opt in channels.items():

        br_quantile = opt['br_quantile']
        br_min = np.quantile(df[ch], br_quantile)

        channel_label = var_to_label[ch]
        color = opt['color']
        alpha = opt['alpha']

        legend_label =  '{} > {:.2e}'.format(channel_label, br_min);

        r = df.query('{} > {}'.format(ch, br_min));

        r.plot.scatter(x=xcol, y=ycol, c=color, alpha=alpha, ax=ax, **scatter_kwargs);

#       ax.scatter(r[xcol], r[ycol], s=30.0, alpha=alpha, c=opt['color'],
#                  **scatter_kwargs)
        ax.scatter(r[0:1][xcol], r[0:1][ycol], label=legend_label, s=30.0, alpha=1.0, c=opt['color'],
                   **scatter_kwargs)

        x_mean = r[xcol].mean()
        y_mean = r[ycol].mean()

#       ax.scatter(x_mean, y_mean, label=legend_label, s=30.0, alpha=1.0, c=opt['color'],
#                  **scatter_kwargs)
        

    xlabel = var_to_label[xcol]
    ylabel = var_to_label[ycol]
    
    ax.set_xlabel(xlabel);
    ax.set_ylabel(ylabel);
    
    return fig, ax


def chi2_levels(df, xcol, ycol, zcol, chi2_bounds, fig=None, ax=None): 
    if ax is None:
        fig,ax = plt.subplots()

    levels = [0.0, chi2_bounds['chi2_sig1_upper_bound'], chi2_bounds['chi2_sig2_upper_bound'], chi2_bounds['chi2_sig3_upper_bound']]

    contourf_kwargs = {'levels': levels, 'colors':chi2_nsigma_colors}
    fig, ax = contourf_levels(df, xcol, ycol, zcol, contourf_kwargs=contourf_kwargs, fig=fig, ax=ax)

    return fig,ax


##################################################################################
#################################
### --- Utility functions --- ###
#################################

def create_legend_sidebox(labels, legends):

    f,a = plt.subplots(figsize=(4,8))
    a.grid(False)

    a.set_xticks(())
    a.set_yticks(())

    vspace = 0.07 

    xpos = 0.05
    ypos_start = 0.93

    for i,label in enumerate(labels):
        a.text(xpos, ypos_start-i*vspace, label, transform=a.transAxes, fontsize=15)


    for legend in legends:

        color      = var_to_color[legend]
        marker     = var_to_marker[legend]
        markersize = var_to_markersize.get(legend)
        linewidth  = var_to_linewidth[legend]
        facecolor  = var_to_facecolor.get(legend, color)
        edgecolor  = var_to_edgecolor.get(legend, color)
        alpha      = var_to_alpha[legend]

        legend_label = var_to_label[legend]
        a.scatter(-1, -1, marker=marker, s=markersize, linewidth=linewidth, edgecolor=edgecolor,
                 facecolor=facecolor, label=legend_label)

    a.set_xlim(0.0, 1.0)
    a.legend(loc=(-0.02, 0.2), frameon=False, fontsize=15, labelspacing=1)
    return f,a


def contourf_levels(df, xcol, ycol, zcol, contourf_kwargs={}, colorbar_kwargs=None, fig=None, ax=None):

    if ax is None:
        fig,ax = plt.subplots()

    dfmesh = df.pivot(xcol, ycol, zcol)
    xi, yi, zi = dfmesh.index.values, dfmesh.columns.values, dfmesh.values.T

    cs = ax.contourf(xi, yi, zi, **contourf_kwargs)

    if colorbar_kwargs is not None:
        cb = fig.colorbar(cs, ax=ax, **colorbar_kwargs)

    return fig, ax


def contour_levels(df, xcol, ycol, zcol, contour_kwargs={}, clabel_kwargs=None, fig=None, ax=None):

    if ax is None:
        fig,ax = plt.subplots()

    dfmesh = df.pivot(xcol, ycol, zcol)
    xi, yi, zi = dfmesh.index.values, dfmesh.columns.values, dfmesh.values.T

    cs = ax.contour(xi, yi, zi, **contour_kwargs)

    if clabel_kwargs is not None:
        ax.clabel(cs, **clabel_kwargs)

    return fig, ax

def set_axis_limits(ax):

    xlabel = ax.xaxis.get_label().get_text()
    ylabel = ax.yaxis.get_label().get_text()

    if xlabel in axis_label_to_limits:
        ax.set_xlim(axis_label_to_limits[xlabel])
    if ylabel in axis_label_to_limits:
        ax.set_ylim(axis_label_to_limits[ylabel])

    return ax


#######################
### --- Various --- ###
#######################

def cba_tb_theory_plot(df):
    
    sta_excl = df.query('sta == 0')
    per_excl = df.query('per_8pi == 0')
    uni_excl = df.query('uni == 0')
    
    f,a = plt.subplots()

    per_excl.plot.scatter('cba', 'tb', rasterized=True, marker='s', s=30, c='white', facecolor='None', edgecolor='magenta', alpha=0.8, ax=a)
    sta_excl.plot.scatter('cba', 'tb', rasterized=True, marker='x', s=30, linewidth=1, c='k', ax=a)
    uni_excl.plot.scatter('cba', 'tb', rasterized=True, marker='o', c='blue', ax=a)

    a.set_xlabel(r'$\cos(\beta - \alpha)$')
    a.set_ylabel(r'$\tan \beta$')

    a.set_xlim(-0.65, 0.65)
    a.set_ylim(1.0, 22)
    return f,a
