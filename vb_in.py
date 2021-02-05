from priors import *

jobctl = {
    "trials" : {
        "Pfizer (Final)" : {"n_p":162, "n_v":8, "v2p_ratio":1.0, "xlo":0.75},
        "Pfizer (Severe)" : {"n_p": 9, "n_v": 1, "v2p_ratio":1.0, "xlo":0.0},
        "Moderna (Interim)" : {"n_p":90, "n_v":5, "v2p_ratio":1.0, "xlo":0.70},
        "Moderna (Final)" : {"n_p":185, "n_v":11, "v2p_ratio":1.0, "xlo":0.75},
        "Moderna (Severe)" : {"n_p": 30, "n_v":0, "v2p_ratio":1.0, "xlo":0.70},
        "Sputnik V (Final)" : {"n_p":62, "n_v":16, "v2p_ratio":3.0, "xlo":0.70},
        "Sputnik V (Moderate+Severe)" : {"n_p":20, "n_v":0, "v2p_ratio":3.0, "xlo":0.7},
        # "AstraZeneca SD+SD" : {"n_p":71, "n_v":27, "v2p_ratio":1.0, "xlo": 0.3},
        # "AstraZeneca LD+SD" : {"n_p":30, "n_v":3, "v2p_ratio":1.0, "xlo":0.3},
        "AstraZeneca SD+SD" : {"n_p":197, "n_v":74, "v2p_ratio":1.0, "xlo": 0.3},
        "AstraZeneca SD+SD T2-T1 < 6 wks " : {"n_p":76, "n_v":35, "v2p_ratio":1.0, "xlo": 0.1},
        "AstraZeneca SD+SD T2-T1 = 6-8 wks " : {"n_p":44, "n_v":20, "v2p_ratio":1.1, "xlo": 0.1},
        "AstraZeneca SD+SD T2-T1 = 9-11 wks " : {"n_p":32, "n_v":11, "v2p_ratio":0.95, "xlo": 0.1},
        "AstraZeneca SD+SD T2-T1 > 12 wks " : {"n_p":45, "n_v":8, "v2p_ratio":0.95, "xlo": 0.1},
        "AstraZeneca LD+SD" : {"n_p":51, "n_v":10, "v2p_ratio":1.0, "xlo":0.3},
        "AstraZeneca B.1.1.7" : {"n_p":27, "n_v":7, "v2p_ratio":1.0, "xlo":0.2},
        "AstraZeneca Non-B.1.1.7" : {"n_p":74, "n_v":12, "v2p_ratio":1.0, "xlo":0.2},
        "AstraZeneca Single Dose, 22-90 days" :{"n_p":71, "n_v":17, "v2p_ratio":1.0, "xlo":0.3},
        "Novavax UK Phase 3" : {"n_p":56, "n_v":6, "v2p_ratio":1.0, "xlo":0.3},
        "Novavax S. Africa Phase 2b" : {"n_p":29, "n_v":15, "v2p_ratio":1.0, "xlo":0.0},
        "J&J Guessed Data" : {"n_p":349, "n_v":119, "v2p_ratio":1.0, "xlo":0.4},
        "Sinovac (Interim, Turkey)": {"n_p":26, "n_v":3, "v2p_ratio":752.0/570.0, "xlo":0.3},
    },
    "cred": 0.90, # Probability level of credible regions
    "cred_lb" : 0.99, # Probability level of lower bound
    "nsamp" : 1000, # Number of equal-spaced samples in [0,1] for the posterior
    "prior" : uniform_prior, # Prior choice, from 'priors.py'
}
