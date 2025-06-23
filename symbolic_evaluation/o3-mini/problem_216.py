import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute Gamma(1/8)
gamma_18 = mp.gamma(mp.mpf(1)/8)

# Compute Gamma(3/8)
gamma_38 = mp.gamma(mp.mpf(3)/8)

# Compute the hypergeometric function 0F1(;1/2;-1)
hyper = mp.hyper([], [mp.mpf(1)/2], -1)

# Compute the constant factor: 1/(2 * sqrt(pi))
constant = 1 / (2 * mp.sqrt(mp.pi))

# Combine all components to get the result
result = constant * gamma_18 * gamma_38 * hyper

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))