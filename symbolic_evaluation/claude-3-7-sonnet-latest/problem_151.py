import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Calculate gamma function at 1/4
gamma_val = mp.gamma(1/4)

# Square the gamma value
gamma_sq = gamma_val ** 2

# Compute the result: (2 * pi^2) / [gamma(1/4)]^2
result = (2 * pi_sq) / gamma_sq

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))