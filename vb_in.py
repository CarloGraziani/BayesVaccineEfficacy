from priors import *

jobctl = {
    "trials" : {
        "Pfizer (Final)" : {"n_p":162, "n_v":8, "v2p_ratio":1.0, "xlo":0.0},
        "Pfizer (Severe)" : {"n_p": 9, "n_v": 1, "v2p_ratio":1.0, "xlo":0.0},
        "Pfizer (14 days after dose1 to dose 2)": {"n_p":27, "n_v":2, "v2p_ratio":1.0, "xlo":0.0},
        "Moderna (Final)" : {"n_p":185, "n_v":11, "v2p_ratio":1.0, "xlo":0.0},
        "Moderna (Severe)" : {"n_p": 30, "n_v":0, "v2p_ratio":1.0, "xlo":0.0},
        "Moderna (14 days after dose 1 to dose 2)" : {"n_p": 35, "n_v":2, "v2p_ratio":1.0, "xlo":0.0},
        "Moderna (>14 days after single dose)" : {"n_p": 28, "n_v":2, "v2p_ratio":0.92, "xlo":0.0},
        "Sputnik V (Final)" : {"n_p":62, "n_v":16, "v2p_ratio":3.0, "xlo":0.0},
        "Sputnik V (Moderate+Severe)" : {"n_p":20, "n_v":0, "v2p_ratio":3.0, "xlo":0.0},
        "AstraZeneca SD+SD" : {"n_p":197, "n_v":74, "v2p_ratio":1.0, "xlo": 0.0},
        "AstraZeneca SD+SD T2-T1 < 6 wks " : {"n_p":76, "n_v":35, "v2p_ratio":1.0, "xlo": 0.0},
        "AstraZeneca SD+SD T2-T1 = 6-8 wks " : {"n_p":44, "n_v":20, "v2p_ratio":1.1, "xlo": 0.0},
        "AstraZeneca SD+SD T2-T1 = 9-11 wks " : {"n_p":32, "n_v":11, "v2p_ratio":0.95, "xlo": 0.0},
        "AstraZeneca SD+SD T2-T1 > 12 wks " : {"n_p":45, "n_v":8, "v2p_ratio":0.95, "xlo": 0.0},
        "AstraZeneca LD+SD" : {"n_p":51, "n_v":10, "v2p_ratio":1.0, "xlo":0.0},
        "AstraZeneca B.1.1.7" : {"n_p":27, "n_v":7, "v2p_ratio":1.0, "xlo":0.0},
        "AstraZeneca Non-B.1.1.7" : {"n_p":74, "n_v":12, "v2p_ratio":1.0, "xlo":0.0},
        "AstraZeneca Single Dose, 22-90 days" :{"n_p":71, "n_v":17, "v2p_ratio":1.0, "xlo":0.0},
        "Novavax UK Phase 3" : {"n_p":56, "n_v":6, "v2p_ratio":1.0, "xlo":0.0},
        "Novavax S. Africa Phase 2b" : {"n_p":29, "n_v":15, "v2p_ratio":1.0, "xlo":0.0},
        "J&J Guessed Data" : {"n_p":349, "n_v":119, "v2p_ratio":1.0, "xlo":0.0},
        "J&J Overall" : {"n_p":348, "n_v":116, "v2p_ratio":1.0, "xlo":0.0},
        "J&J North America":{"n_p":196, "n_v":51, "v2p_ratio":1.0, "xlo":0.0},
        "J&J Brazil":{"n_p":114, "n_v":39, "v2p_ratio":1.0, "xlo":0.0},
        "J&J South Africa":{"n_p":90, "n_v":43, "v2p_ratio":1.0, "xlo":0.0},
        "J&J Severe":{"n_p":60, "n_v":14, "v2p_ratio":1.0, "xlo":0.0},
        "J&J Severe, North America":{"n_p":18, "n_v":4, "v2p_ratio":1.0, "xlo":0.0},
        "J&J Severe, Brazil":{"n_p":11, "n_v":2, "v2p_ratio":1.0, "xlo":0.0},
        "J&J Severe, South Africa":{"n_p":30, "n_v":8, "v2p_ratio":1.0, "xlo":0.0},
        "Sinovac (Interim, Turkey)": {"n_p":26, "n_v":3, "v2p_ratio":752.0/570.0, "xlo":0.0},
        "COVAXIN (preliminary)": {"n_p":36, "n_v":7, "v2p_ratio":1.0, "xlo":0.0}
    },
    "cred": 0.90, # Probability level of credible regions
    "cred_lb" : 0.99, # Probability level of lower bound
    "nsamp" : 1000, # Number of equal-spaced samples in [0,1] for the posterior
    "prior" : uniform_prior, # Prior choice, from 'priors.py'
}
