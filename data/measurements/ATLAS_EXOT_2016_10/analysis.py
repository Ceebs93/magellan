import os
import pandas as pd
import numpy as np

from measurement.measurement import Measurement
from measurement.measurement import UpperLimitData
import magellan.config as magconf
import hepdata.hepdata as hepdata

limit_vs_mA_GammaA_path = os.path.join(magconf.paths['measurements'], 'ATLAS_EXOT_2016_10', './limit_vs_mA_Gamma_A.dat')

m = Measurement(
               data        = UpperLimitData.from_datafile(limit_vs_mA_GammaA_path, independent_variables=['mA','GammaA_div_mA']),
               description = "ATLAS Higgs A -> Zh, sqrt(s) = 13 TeV, lumi = 36 fb-1",
               tag         = "ATLAS_EXOT_2016_10",
               label       = "ATLAS-EXOT-2016-10",
               process     = r"$A \rightarrow Zh$",
               factor      = 1.0,
               observables = {
                               "xsec_sushi_ggh_A_NNLO_x_br_A_Zh":
                               {"upper_limit" : {"function" : None,
                                                "arguments" : ["mA" , "GammaA_div_mA", "br_h_bb"]}}
                             },
               CL          = 0.95,
               sqrt_s      = 13.0,
               luminosity  = 36.0,
               url         = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/EXOT-2016-10/",
               comment     = ""
               ) 


def limit_vs_mA_GammaA_interpolation_function(vars, limit_type='limit_exp'):

    interpolation_function = m.data['interpolation'][limit_type]['function']

    if isinstance(vars, pd.DataFrame):
        mA = vars.iloc[:,0]
        GammaA_div_mA = vars.iloc[:,1]
        br_h_bb = vars.iloc[:,2]
        values = interpolation_function(mA, GammaA_div_mA)/br_h_bb
    else:
        mA = vars[0]
        GammaA_div_mA = vars[1]
        br_h_bb = vars[2]
        values = interpolation_function(mA, GammaA_div_mA)/0.5809

    return values


m.observables["xsec_sushi_ggh_A_NNLO_x_br_A_Zh"]["upper_limit"]["function"] = limit_vs_mA_GammaA_interpolation_function
