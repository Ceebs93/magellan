#!/usr/bin/env python

from collections import defaultdict


var_to_color = defaultdict(
			  lambda: 'orange',
			   {
 				'sta'         : 'black',
				'per_4pi'     : 'white',
				'per_8pi'     : 'white',
				'uni'         : 'white',
				'sigma1'      : 'gold',
				'sigma2'      : 'forestgreen',
				'sigma3'      : 'navy',
                'HiggsBounds' : 'red'
		       }
			)


var_to_marker = defaultdict(
			  lambda: 'forestgreen',
                {
					'sta'         : 'x',
					'per_4pi'     : 's',
					'per_8pi'     : 's',
					'uni'         : 'o',
					'HiggsBounds' : '+',
        			'sigma1'      : 's',
	    			'sigma2'      : 's',
	    			'sigma3'      : 's'
				}
				)

var_to_linewidth = defaultdict(
     			   lambda: '1',
                   {
			     		'sta'     : 1,
			     		'per_4pi' : 1.0,
			     		'per_8pi' : 1.0,
			     		'uni'     : 1,
			     		'HiggsBounds' : 2.0
			    	}
				   )

var_to_alpha = defaultdict(
     			   lambda: '1.0',
               {
			      'sta'     : 1.0,
			      'per_4pi' : 1.0,
			      'per_8pi' : 1.0,
			      'uni'     : 1.0,
			      'HiggsBounds'  : 1.0
			   }
			   )


var_to_facecolor = { 
						'uni'     : 'None',
						'per_4pi' : 'None',
						'per_8pi' : 'None',
            			'sigma1'  : var_to_color.get('sigma1'),
    	    			'sigma2'  : var_to_color.get('sigma2'),
    	    			'sigma3'  : var_to_color.get('sigma3')
				   }

var_to_edgecolor = { 
						'uni'     : 'navy',
						'per_4pi' : 'magenta',
						'per_8pi' : 'magenta',
						'HiggsBounds'  : 'red'
				   }

var_to_markersize = defaultdict(
                        lambda : 10,
                    {
	     				'sta'     : 40,
	     				'per_4pi' : 40,
	     				'per_8pi' : 40,
	     				'uni'     : 10,
	     				'HiggsBounds'  : 40,
            			'sigma1'  : 40,
    	    			'sigma2'  : 40,
    	    			'sigma3'  : 40
	     			})

chi2_nsigma_to_color = {
						  1 : 'gold',
						  2 : 'forestgreen',
						  3 : 'navy'
					   }


cat_to_color = {
				'alignment'  : 'navy',
				'wrong_sign' : 'firebrick',
				'excluded'   : 'firebrick',
				'all'        : 'navy'
		       }


chi2_nsigma_colors = ['gold', 'forestgreen', 'navy', 'white']

var_to_label = { 
    'mH'                                           : r'$m_{H}$ [GeV]',
    'mHc'                                          : r'$m_{H^{\pm}}$ [GeV]',
    'mA'                                           : r'$m_{A}$ [GeV]',
    'mH_minus_mHc'                                 : r'$m_{H} - m_{H^{\pm}}$ [GeV]',
    'mA_minus_mHc'                                 : r'$m_{A} - m_{H^{\pm}}$ [GeV]',
    'GammaA'                                       : r'$\Gamma_{A}$',
    'Gamma_A'                                      : r'$\Gamma_{A}$',
    'GammaA_div_mA'                                : r'$\Gamma_{A}/m_{A}$',
    'GammaH_div_mH'                                : r'$\Gamma_{H}/m_{H}$',
    'Z4'                                           : r'$Z_{4}$',
    'Z5'                                           : r'$Z_{5}$',
    'Z7'                                           : r'$Z_{7}$',
    'm12'                                          : r'$|m_{12}|$ [GeV]',
    'm12_2'                                        : r'$m_{12}^{2}$ [GeV$^{2}$]',
    'l1'                                           : r'$\lambda_{1}$',
    'l2'                                           : r'$\lambda_{2}$',
    'l3'                                           : r'$\lambda_{3}$',
    'l4'                                           : r'$\lambda_{4}$',
    'l5'                                           : r'$\lambda_{5}$',
    'l6'                                           : r'$\lambda_{6}$',
    'l7'                                           : r'$\lambda_{7}$',
    'lambda_Hhh'                                   : r'$\lambda_{Hhh}$',
    'cba'                                          : r'$\cos(\beta - \alpha)$',
    'tb'                                           : r'$\tan \beta $',
    'chi2_HS'                                      : r'$\chi^{2}_{\mathrm{HS}}$',
    'chi2_Tot_gfitter'                             : r'$\chi^{2}_{\mathrm{HS}}$ + $\chi^{2}_{\mathrm{GFitter}}$',
    'chi2_ST_gfitter'                              : r'$\chi^{2}_{\mathrm{GFitter}}$',
    'xsec_sushi_ggh_A_NNLO'                        : r'$\sigma(gg\rightarrow A)$ [pb]',
    'log_xsec_sushi_ggh_A_NNLO'                    : r'$\log_{10} \sigma(gg\rightarrow A)$ [pb]',
    'xsec_sushi_ggh_H_NNLO'                        : r'$\sigma(gg\rightarrow H)$ [pb]',
    'log_xsec_sushi_ggh_H_NNLO'                    : r'$\log_{10} \sigma(gg\rightarrow H)$ [pb]',
    'xsec_sushi_ggh_A_NNLO_x_br_A_Zh'              : r'$\sigma(gg\rightarrow A) \times Br(A \rightarrow Zh)$ [pb]',
    'xsec_sushi_ggh_A_NNLO_x_br_A_ZH'              : r'$\sigma(gg\rightarrow A) \times Br(A \rightarrow ZH)$ [pb]',
    'xsec_sushi_ggh_A_NNLO_x_br_A_tautau'          : r'$\sigma(gg\rightarrow A) \times Br(A \rightarrow \tau \tau)$ [pb]',    
    'xsec_sushi_ggh_A_NNLO_x_br_A_tt'              : r'$\sigma(gg\rightarrow A) \times Br(A \rightarrow tt)$ [pb]',  
    'xsec_sushi_ggh_A_NNLO_x_br_A_bb'              : r'$\sigma(gg\rightarrow A) \times Br(A \rightarrow bb)$ [pb]',  
    'xsec_sushi_ggh_H_NNLO_x_br_H_Zh'              : r'$\sigma(gg\rightarrow H) \times Br(H \rightarrow Zh)$ [pb]',
    'xsec_sushi_ggh_H_NNLO_x_br_H_AA'              : r'$\sigma(gg\rightarrow H) \times Br(H \rightarrow AA)$ [pb]',    
    'xsec_sushi_ggh_H_NNLO_x_br_H_hh'              : r'$\sigma(gg\rightarrow H) \times Br(H \rightarrow hh)$ [pb]',    
    'xsec_sushi_ggh_H_NNLO_x_br_H_hh_x_br_hh_bbbb' : r'$\sigma(gg\rightarrow H) \times Br(H \rightarrow hh \rightarrow bbbb)$ [pb]',    
    'xsec_sushi_ggh_H_NNLO_x_br_H_Zh'              : r'$\sigma(gg\rightarrow H) \times Br(H \rightarrow Zh)$ [pb]',
    'xsec_sushi_ggh_H_NNLO_x_br_H_ZZ'              : r'$\sigma(gg\rightarrow H) \times Br(H \rightarrow ZZ)$ [pb]',
    'xsec_sushi_ggh_H_NNLO_x_br_H_ZA'              : r'$\sigma(gg\rightarrow H) \times Br(H \rightarrow ZA)$ [pb]',    
    'xsec_sushi_ggh_H_NNLO_x_br_H_tt'              : r'$\sigma(gg\rightarrow H) \times Br(H \rightarrow tt)$ [pb]',    
    'xsec_sushi_ggh_H_NNLO_x_br_H_bb'              : r'$\sigma(gg\rightarrow H) \times Br(H \rightarrow bb)$ [pb]',    
    'xsec_sushi_ggh_H_NNLO_x_br_H_tautau'          : r'$\sigma(gg\rightarrow H) \times Br(H \rightarrow \tau \tau)$ [pb]',    
    'log_xsec_sushi_ggh_H_NNLO_x_br_H_ZA'          : r'$\log_{10} \sigma(gg\rightarrow H) \times Br(H \rightarrow ZA)$ [pb]',    
    'k_hdd'                                        : r'$\kappa_{hdd}$',
    'k_huu'                                        : r'$\kappa_{huu}$',
    'k_hdd_sqr'                                    : r'$\kappa^{2}_{hdd}$',
    'k_huu_sqr'                                    : r'$\kappa^{2}_{huu}$',
    'br_h_bb'                                      : r'$\mathcal{B}r(h \rightarrow bb)$',
    'br_H_ZA'                                      : r'$\mathcal{B}r(H \rightarrow ZA)$',
    'br_A_Zh'                                      : r'$\mathcal{B}r(A \rightarrow Zh)$',
    'br_A_ZH'                                      : r'$\mathcal{B}r(A \rightarrow ZH)$',
    'br_A_tautau'                                  : r'$\mathcal{B}r(A \rightarrow \tau \tau)$',
    'br_A_ZH'                                      : r'$\mathcal{B}r(A \rightarrow ZH)$',
    'br_A_bb'                                      : r'$\mathcal{B}r(A \rightarrow bb)$',
    'br_A_tt'                                      : r'$\mathcal{B}r(A \rightarrow tt)$',
    'br_A_gaga'                                    : r'$\mathcal{B}r(A \rightarrow \gamma \gamma)$',
    'br_H_tautau'                                  : r'$\mathcal{B}r(H \rightarrow \tau \tau)$',
    'br_H_Zh'                                      : r'$\mathcal{B}r(H \rightarrow Zh)$',
    'br_H_tt'                                      : r'$\mathcal{B}r(H \rightarrow tt)$',
    'br_H_bb'                                      : r'$\mathcal{B}r(H \rightarrow bb)$',
    'br_H_ZA'                                      : r'$\mathcal{B}r(H \rightarrow ZA)$',
    'br_H_AA'                                      : r'$\mathcal{B}r(H \rightarrow AA)$',
    'br_H_gaga'                                    : r'$\mathcal{B}r(H \rightarrow \gamma \gamma)$',
    'br_H_hh'                                      : r'$\mathcal{B}r(H \rightarrow hh)$',
	'S'                                            : r'$S$',
	'T'                                            : r'$T$',
	'U'                                            : r'$U$',
	'uni'                                          : r'Excl. by unitarity',
	'sta'                                          : r'Excl. by stability',
	'per_4pi'                                      : r'Excl. by perturbativity ($4 \pi$)',
	'per_8pi'                                      : r'Excl. by perturbativity ($8 \pi$)',
	'HiggsBounds'                                  : r'Excl. by HiggsBound',
    'sigma1'                                       : r'Allowed 1 $\sigma$ HiggsSignals',
    'sigma2'                                       : r'Allowed 2 $\sigma$ HiggsSignals',
    'sigma3'                                       : r'Allowed 3 $\sigma$ HiggsSignals',
    'limit_exp'                                    : r'exp. limit',
    'limit_obs'                                    : r'obs. limit',
    'stay_count'                                   : r'Stay count'
}


A_channels = {
               'br_A_tt'     : {'br_min' : 0.90, 'color' : 'firebrick',     'alpha' : 0.05 },
               'br_A_Zh'     : {'br_min' : 0.80, 'color' : 'navy',          'alpha' : 0.10 },
               'br_A_ZH'     : {'br_min' : 0.80, 'color' : 'lightseagreen', 'alpha' : 0.10 },
               'br_A_tautau' : {'br_min' : 0.10, 'color' : 'gold',          'alpha' : 0.30 },
               'br_A_bb'     : {'br_min' : 0.70, 'color' : 'forestgreen',   'alpha' : 0.05 }
             }

H_channels = {
               'br_H_tt'     : {'br_min' : 0.90, 'color' : 'firebrick',     'alpha' : 0.05 },
               'br_H_AA'     : {'br_min' : 0.01, 'color' : 'navy',          'alpha' : 0.20 },
               'br_H_ZA'     : {'br_min' : 0.80, 'color' : 'lightseagreen', 'alpha' : 0.10 },
               'br_H_tautau' : {'br_min' : 0.10, 'color' : 'gold',          'alpha' : 0.30 },
               'br_H_bb'     : {'br_min' : 0.70, 'color' : 'forestgreen',   'alpha' : 0.05 }
             }

analyses = {
             175 : {'ch': r'$Z h$ / VBF, $h \rightarrow$ invisible', 'analysis' : '1404.1344 (CMS)',     'marker' :'o', 'color' : 'forestgreen', 'alpha' : 0.1},
             211 : {'ch': r'$h \rightarrow WW$',                     'analysis' : 'ATLAS-CONF-2012-012', 'marker' :'v', 'color' : 'deepskyblue', 'alpha' : 0.1},
             226 : {'ch': r'$h \rightarrow WW$',                     'analysis' : 'CMS-PAS-HIG-13-022',  'marker' :'^', 'color' : 'plum',        'alpha' : 0.1},
             269 : {'ch': r'$H \rightarrow ZZ \rightarrow 4l$',      'analysis' : 'ATLAS-CONF-2013-013', 'marker' :'o', 'color' : 'navy',        'alpha' : 0.1},
             277 : {'ch': r'$h \rightarrow ZZ \rightarrow 4l$',      'analysis' : 'CMS-PAS-HIG-13-002',  'marker' :'s', 'color' : 'olivedrab',   'alpha' : 0.1},
             281 : {'ch': r'$H \rightarrow ZZ \rightarrow 4l$',      'analysis' : 'CMS-PAS-HIG-13-002',  'marker' :'p', 'color' : 'magenta',     'alpha' : 0.1},
             284 : {'ch': r'$H \rightarrow VV$',                     'analysis' : '1504.00936 (CMS)',    'marker' :'o', 'color' : 'navy',        'alpha' : 0.1},
             337 : {'ch': r'$h$ combination',                        'analysis' : 'CMS-PAS-HIG-12-045',  'marker' :'P', 'color' : 'gold',        'alpha' : 0.1},
             368 : {'ch': r'$H \rightarrow hh$',                     'analysis' : '1509.04670 (ATLAS)',  'marker' :'H', 'color' : 'red',         'alpha' : 0.3},
             422 : {'ch': r'$H \rightarrow \gamma \gamma$',          'analysis' : '1407.6583 (ATLAS)',   'marker' :'D', 'color' : 'silver',      'alpha' : 0.4},
             423 : {'ch': r'$A \rightarrow \gamma \gamma$',          'analysis' : '1407.6583 (ATLAS)',   'marker' :'8', 'color' : 'black',       'alpha' : 0.3},
             425 : {'ch': r'$h \rightarrow WW$',                     'analysis' : '1507.05930 (ATLAS)',  'marker' :'*', 'color' : 'crimson',     'alpha' : 0.2},
             553 : {'ch': r'$H \rightarrow \tau \tau$',              'analysis' : 'CMS-HIG-PAS 14-029',  'marker' :'3', 'color' : 'darkorange',  'alpha' : 0.1},
             554 : {'ch': r'$A \rightarrow \tau \tau$',              'analysis' : 'CMS-HIG-PAS 14-029',  'marker' :'4', 'color' : 'greenyellow', 'alpha' : 0.9},
           }

# - Holoviews variables
hv_v      = {
            'cba':                                 ('cba',         'cos(b-a)'),
            'tb':                                  ('tb',          'tan(b)'),
            'mH':                                  ('mH',          'mH [GeV]'),
            'mHc':                                 ('mHc',         'mH+ [GeV]'),
            'mA':                                  ('mA',          'mA [GeV]'),
            'mA':                                  ('mA',          'mA [GeV]'),
            'mA_bin':                              ('mA_bin',      'mA [GeV] (bin center)'),
            'Z7':                                  ('Z7',          'Z7'),
            'Gamma_A':                             ('Gamma_A',     'Gamma_A [GeV]'),
            'br_h_bb':                             ('br_h_bb',     'Br(h->bb)'),
            'br_H_bb':                             ('br_H_bb',     'Br(H->bb)'),
            'br_H_tt':                             ('br_H_tt',     'Br(H->tt)'),
            'br_H_tautau':                         ('br_H_tautau', 'Br(H->tautau)'),
            'br_H_hh':                             ('br_H_hh',     'Br(H->hh)'),
            'br_H_ZA':                             ('br_H_ZA',     'Br(H->ZA)'),
            'br_H_AA':                             ('br_H_AA',     'Br(H->AA)'),
            'br_A_bb':                             ('br_A_bb',     'Br(A->bb)'),
            'br_A_Zh':                             ('br_A_Zh',     'Br(A->Zh)'),
            'br_A_ZH':                             ('br_A_ZH',     'Br(A->ZH)'),
            'br_A_tautau':                         ('br_A_tautau', 'Br(A->tau tau)'),
            'br_A_tt':                             ('br_A_tt',     'Br(A->tt)'),
            'GammaA_div_mA':                       ('GammaA_div_mA', 'GammaA / mA'),
            'GammaH_div_mH':                       ('GammaH_div_mH', 'GammaH / mH'),
            'xsec_sushi_ggh_H_NNLO':               ('xsec_sushi_ggh_H_NNLO',               'sig(H) [pb]'),
            'xsec_sushi_ggh_A_NNLO':               ('xsec_sushi_ggh_A_NNLO',               'sig(A) [pb]'),
            'xsec_sushi_ggh_A_NNLO_x_br_A_Zh':     ('xsec_sushi_ggh_A_NNLO_x_br_A_Zh',     'sig(A)xBr(A->Zh) [pb]'),
            'xsec_sushi_ggh_A_NNLO_x_br_A_tautau': ('xsec_sushi_ggh_A_NNLO_x_br_A_tautau', 'sig(A)xBr(A->tau tau) [pb]'),
            'xsec_sushi_ggh_A_NNLO_x_br_A_tt':     ('xsec_sushi_ggh_A_NNLO_x_br_A_tt',     'sig(A)xBr(A->tt) [pb]'),
            'xsec_sushi_ggh_A_NNLO_x_br_A_bb':     ('xsec_sushi_ggh_A_NNLO_x_br_A_bb',     'sig(A)xBr(A->bb) [pb]'),
            'xsec_sushi_ggh_H_NNLO_x_br_H_bb':     ('xsec_sushi_ggh_H_NNLO_x_br_H_bb',     'sig(H)xBr(H->bb) [pb]'),
            'xsec_sushi_ggh_H_NNLO_x_br_H_hh':     ('xsec_sushi_ggh_H_NNLO_x_br_H_hh',     'sig(H)xBr(H->hh) [pb]'),
            'xsec_sushi_ggh_H_NNLO_x_br_H_ZA':     ('xsec_sushi_ggh_H_NNLO_x_br_H_ZA',     'sig(H)xBr(H->ZA) [pb]'),
            'xsec_sushi_ggh_H_NNLO_x_br_H_tt':     ('xsec_sushi_ggh_H_NNLO_x_br_H_tt',     'sig(H)xBr(H->tt) [pb]'),
            'xsec_sushi_ggh_H_NNLO_x_br_H_tautau': ('xsec_sushi_ggh_H_NNLO_x_br_H_tautau', 'sig(H)xBr(H->tautau) [pb]'),
            'xsec_sushi_ggh_H_NNLO_x_br_H_hh_x_br_hh_bbbb' : ('xsec_sushi_ggh_H_NNLO_x_br_H_hh_x_br_hh_bbbb', 'sig(H)xBr(H->hh->bbbb) [pb]')
          }

### --- Axis limtis -- ###

axis_label_to_limits = {
                var_to_label['mA']  : (200.0, 1000.0),
                var_to_label['mH']  : (200.0, 1000.0),
                var_to_label['mHc'] : (550.0 ,1000.0),
                var_to_label['tb']  : (0.0 , 30.0),
              }

var_to_limit = {
                'mA'                                  : (200.0, 1000.0),
                'mH'                                  : (200.0, 1000.0),
                'xsec_sushi_ggh_A_NNLO_x_br_A_Zh'     : (1e-4, 10.0),
                'xsec_sushi_ggh_H_NNLO_x_br_H_tautau' : (1e-5, 1.0),
                'xsec_sushi_ggh_A_NNLO_x_br_A_tautau' : (1e-4, 1.0),
                'xsec_sushi_ggh_H_NNLO_x_br_H_hh'     : (1e-3, 6.0),
                'xsec_sushi_ggh_H_NNLO_x_br_H_hh_x_br_hh_bbbb' : (1e-5, 6.0)
               }


log_axes = ['xsec_sushi_ggh_A_NNLO_x_br_A_Zh',
            'xsec_sushi_ggh_H_NNLO_x_br_H_tautau',
            'xsec_sushi_ggh_H_NNLO_x_br_H_hh',
            'xsec_sushi_ggh_H_NNLO_x_br_H_hh_x_br_hh_bbbb',
            'xsec_sushi_ggh_A_NNLO_x_br_A_tautau'
           ]
            
