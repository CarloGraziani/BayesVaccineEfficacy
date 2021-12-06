#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from priors import *
import sys
sys.path.insert(0,".")

############## Job Control ##################################
# Default values, overridden by vbe_in.py
#
jobctl_0 = {
    "samples" : {
        "UK-Omicron-20211203" : {"n_p":10, "n_v":12, "v2p_ratio":4.263, "xlo":0.0},
        "Israel-Omicron-20211206" : {"n_p":8, "n_v":13, "v2p_ratio":8.17, "xlo":0.0},
        },
    "cred": 0.90, # Probability level of credible regions
    "cred_lb" : 0.99, # Probability level of lower bound
    "nsamp" : 1000, # Number of equal-spaced samples in [0,1] for the posterior
    "prior" : uniform_prior, # Prior choice, from 'priors.py'
}

# If vbe_in.py exists and contains a dict called 'jobctl', use it to update jobctl_0
try:
    from vbe_in import jobctl
    jobctl_0.update(jobctl)
    print("Imported job from vbe_in.py")
except ImportError:
    print("No job imported, using defaults")
    pass

# All keys in jobctl_0 now to become variables:
globals().update(jobctl_0)

################## Done with job control #####################

cs="%4.1f"%(cred*100.0)
de = 1.0 / nsamp
eff = de * (np.arange(nsamp, dtype=float) + 0.5 )

def loglik(e,sample):
    ll = sample["n_v"] * np.log(1.0-e) - \
         (sample["n_p"] + sample["n_v"]) * np.log(1.0 + (1-e)*sample["v2p_ratio"])
    return ll

posterior = np.zeros(nsamp)
eff_ci = np.zeros(2)
fsize=16
fsize_l=12
lw_ci=2
lw_plot=3
msize=18

for samplename in samples.keys():

    sample = samples[samplename]

    ll = loglik(eff, sample)
    pr = prior(eff)
    llmax = np.max(ll)
    posterior = np.exp(ll - llmax) * pr
    norm = posterior.sum() * de
    posterior /= norm
    inds = np.argsort(posterior)[-1::-1]
    cum = posterior[inds].cumsum() * de
    lbcum = posterior[-1::-1].cumsum() * de
    lb_ind = nsamp-np.searchsorted(lbcum, cred_lb)
    eff_lb = eff[lb_ind]
    lb_x = list(eff[lb_ind:])
    lb_x.insert(0,eff[lb_ind])
    lb_x.append(eff[-1])
    lb_y = list(posterior[lb_ind:])
    lb_y.insert(0,0.0)
    lb_y.append(0.0)

    eff_mp = eff[inds[0]]
    eff_ci[0] = eff[inds[0]]
    eff_ci[1] = eff[inds[0]]
    ci_idx_lo = ci_idx_hi = inds[0]
    for samp in range(nsamp):
        if eff[inds[samp]] > eff_ci[1]:
            eff_ci[1] = eff[inds[samp]]
            ci_idx_hi = inds[samp]
        if eff[inds[samp]] < eff_ci[0]:
            eff_ci[0] = eff[inds[samp]]
            ci_idx_lo = inds[samp]
        if cum[samp] > cred:
            break
    ci_x = list(eff[ci_idx_lo:ci_idx_hi+1])
    ci_x.insert(0, eff[ci_idx_lo])
    ci_x.append(eff[ci_idx_hi])
    ci_y = list(posterior[ci_idx_lo:ci_idx_hi+1])
    ci_y.insert(0,0.0)
    ci_y.append(0.0)

    print(samplename +
          ": Max Posterior Effectiveness = %6.3f; %4.1f%% CI = [%6.3f, %6.3f]; %4.1f%% Lower Bound = %6.3f\n" %
          (eff_mp, cred*100.0, eff_ci[0], eff_ci[1], cred_lb*100.0, eff_lb) )

    fig = plt.figure()
    fig.set_figwidth(8.0)
    fig.set_figheight(8.0)
    ax = fig.add_subplot(1,1,1)

    ax.set_xlim([sample["xlo"],1.0])
    ax.set_ylim(bottom=0.0, top=posterior[inds[0]]*1.2)
    ax.set_xlabel("Vaccine Effectiveness", size=fsize)
    ax.set_ylabel("Posterior Density", size=fsize)
    ax.tick_params(labelsize=fsize)

    ax.plot(eff,posterior,'b-', linewidth=lw_plot)
    ax.axvline(eff_mp, color="c", linewidth=lw_plot,
               linestyle="--",
               label='Max Posterior: Eff. = %5.3f'%(eff_mp) )

    ax.fill(ci_x, ci_y, color='r', alpha=0.4,
               label='%4.1f%% Credible Region:'%(cred*100) + ' Eff.$\in$'+'[%5.3f,%5.3f]'%
                      (eff_ci[0],eff_ci[1]))
    # ax.axvline(eff_ci[0], color='r', linewidth=lw_ci, linestyle=":")
    # ax.axvline(eff_ci[1], color='r', linewidth=lw_ci, linestyle=":")

    #ax.axvline(eff_lb, color='g', linewidth=lw_ci, linestyle="-.")
    ax.fill(lb_x, lb_y, hatch="/", fill=False,
               label="%4.1f%% Lower Bound: Eff. = %5.3f" % (cred_lb*100, eff_lb))

    ax.legend(handlelength=4.0)

    ax.set_title(samplename + ": Unvaxxed Infections = %d, Vaxxed Infections = %d\n Vaxxed/Unvaxxed Ratio = %4.2f" % (sample["n_p"], sample["n_v"], sample["v2p_ratio"]) )

    plt.savefig(samplename +".png", format="png")
    plt.close(fig)
