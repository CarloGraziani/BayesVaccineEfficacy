from priors import *

jobctl = {
        "samples" : {
        "UK-Omicron-20211203" : {"n_p":10, "n_v":12, "v2p_ratio":4.263, "xlo":0.0},
        "Israel-Omicron-20211206" : {"n_p":8, "n_v":13, "v2p_ratio":8.17, "xlo":0.0},
        },
    "cred": 0.90, # Probability level of credible regions
    "cred_lb" : 0.99, # Probability level of lower bound
    "nsamp" : 1000, # Number of equal-spaced samples in [0,1] for the posterior
    "prior" : uniform_prior, # Prior choice, from 'priors.py'
}
