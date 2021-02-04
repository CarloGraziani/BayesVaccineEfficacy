from priors import *

jobctl = {
    "trials" : {
        "Pfizer (Final)" : {"n_p":262, "n_v":8, "v2p_ratio":1.0, "xlo":0.75},
        "Pfizer (Severe)" : {"n_p": 9, "n_v": 1, "v2p_ratio":1.0, "xlo":0.0},
        "Moderna (Interim)" : {"n_p":90, "n_v":5, "v2p_ratio":1.0, "xlo":0.70},
        "Moderna (Final)" : {"n_p":185, "n_v":11, "v2p_ratio":1.0, "xlo":0.75},
        "Moderna (Severe)" : {"n_p": 30, "n_v":0, "v2p_ratio":1.0, "xlo":0.70},
        "Sputnik V (Interim)" : {"n_p":31, "n_v":8, "v2p_ratio":3.0, "xlo":0.45},
        "AstraZeneca SD+SD" : {"n_p":71, "n_v":27, "v2p_ratio":1.0, "xlo": 0.3},
        "AstraZeneca LD+SD" : {"n_p":30, "n_v":3, "v2p_ratio":1.0, "xlo":0.3},
        "CoronaVac (Interim, Turkey)" : {"n_p":26, "n_v":3, "v2p_ratio":752.0/570.0, "xlo":0.3},
    },
    "cred": 0.90, # Probability level of credible regions
    "cred_lb" : 0.99, # Probability level of lower bound
    "nsamp" : 1000, # Number of equal-spaced samples in [0,1] for the posterior
    "prior" : show_me_prior, # Prior choice, from 'priors.py'
}
