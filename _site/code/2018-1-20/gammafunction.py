import numpy as np
from scipy.special import gamma

def log_gamma_Stirling(z):
    k = z-1.
    return 0.5*np.log(2*np.pi*k) + k*(np.log(k)-1)

def gamma_Stirling(z):
    return np.exp(log_gamma_Stirling(z))


if __name__ == "__main__":
    print gamma(100), gamma_Stirling(100)
    print gamma(1000), gamma_Stirling(1000), log_gamma_Stirling(1000)

    print 'Compare sqrt(n) with mean chi distribution with n parameters'
    for n in [1e4, 1e6, 1e8, 1e10, 1e12]:
        print 'n={:15.1f}, sqrt(n)={:10.1f}, mean(chi_n)={:10.1f}'.format(n, np.sqrt(n),
        np.exp(0.5*np.log(2) + log_gamma_Stirling(0.5*(n+1)) -
        log_gamma_Stirling(0.5*n)))
