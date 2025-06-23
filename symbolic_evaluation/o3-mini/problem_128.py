import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate constant factors
# 2^(1/4)
factor1 = mp.power(2, mp.mpf(1)/4)
# e^(1/2)
factor2 = mp.exp(mp.mpf(1)/2)
# Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)
# Denominator: 2 * sqrt(pi)
denom = 2 * mp.sqrt(mp.pi)

# Combine constant factors: (2^(1/4) * e^(1/2) * Gamma(1/4)) / (2*sqrt(pi))
const_factor = (factor1 * factor2 * gamma_val) / denom

# Compute modified Bessel functions of the first kind
# I_{-1/4}(1/2)
bessel_minus = mp.besseli(-mp.mpf(1)/4, mp.mpf(1)/2)
# I_{1/4}(1/2)
bessel_plus = mp.besseli(mp.mpf(1)/4, mp.mpf(1)/2)

# Take the difference: I_{-1/4}(1/2) - I_{1/4}(1/2)
bessel_diff = bessel_minus - bessel_plus

# Multiply constant factor by the Bessel difference
result = const_factor * bessel_diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))