import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate exponential term: e^{-2.0}
exp_term = mp.exp(-2.0)

# Subtract exponential term from 1
one_minus_exp = 1 - exp_term

# Multiply by pi to get final result
result = mp.pi * one_minus_exp

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))