import mpmath as mp
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate exponent term e^(-1/4)
exponent = -mp.mpf(1)/4
exp_term = mp.exp(exponent)

# Combine components for final result
result = 2 * sqrt_pi * exp_term

print(mp.nstr(result, n=10))