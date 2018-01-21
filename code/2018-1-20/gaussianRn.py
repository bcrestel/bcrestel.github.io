import numpy as np
from numpy.random import standard_normal
import matplotlib.pyplot as plt
from scipy.special import gamma

def concentration_of_measure(nbsamples=1000):
    alldraws = standard_normal(100000*nbsamples)
    # look at different dimension R^n
    for n in [1, 2, 3, 4, 5, 50, 100, 500, 1000, 10000, 100000]:
        draws = alldraws[:n*nbsamples]
        samples = draws.reshape((nbsamples, n))
        dist = np.sqrt((samples**2).sum(axis=1))
        print 'n={:5d}, sqrt(n)={:5.2f}, mean={:5.2f} (std={:5.4f})'.format(
        n, np.sqrt(n), np.mean(dist), np.std(dist)),
        print '\tpercentiles: 25%={:5.2f}, 50%={:5.2f}, 75%={:5.2f}'.format(
        np.percentile(dist, 25), np.percentile(dist, 50), np.percentile(dist,75))

        dist = (samples**2).sum(axis=1)
        print '\t\t\tmean={:5.2f} (std={:5.4f})'.format(np.mean(dist), np.std(dist))

    dist = np.abs(alldraws)
    print 'mean={:5.2f} (std={:5.4f})'.format(
    np.mean(dist), np.std(dist))


def vol_n_sphere(r,n):
    return np.pi**(0.5*n)*(r**n)/gamma(1+0.5*n)
    

def mass_nsphere(n):
    return (vol_n_sphere(1.0,n) - vol_n_sphere(0.99,n))/vol_n_sphere(1.0,n)

def distr_mass_nsphere():
    for n in [10,50,100]:
        print 'n={}, ratio(0.99-1.00)={:.2f}'.format(n, mass_nsphere(n))


if __name__ == "__main__":
    concentration_of_measure(1000)
    distr_mass_nsphere()
