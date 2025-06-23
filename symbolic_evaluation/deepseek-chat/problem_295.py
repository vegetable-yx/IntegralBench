import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide pi squared by 4
term1 = pi_squared / 4

# Compute 1/2 as a precise floating-point number
term2 = mp.mpf(1) / 2

# Sum the two terms
result = term1 + term2

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))