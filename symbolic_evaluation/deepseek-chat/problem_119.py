import mpmath as mp

# Set the internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate pi squared
pi_sq = mp.power(mp.pi, 2)

# Divide pi squared by 8
pi_sq_over_8 = pi_sq / 8

# Compute the constant term 1/2
half = mp.mpf(1) / 2

# Subtract half from pi_sq_over_8
result = pi_sq_over_8 - half

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))