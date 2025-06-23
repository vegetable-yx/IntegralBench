import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide pi squared by 16
term1 = pi_sq / 16

# Compute the constant term 1/2
half = mp.mpf(1) / 2

# Combine terms: π²/16 - 1/2
result = term1 - half

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))