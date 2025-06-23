import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 16 to get first term
term1 = pi_sq / 16

# Calculate second term: 1/8
term2 = mp.mpf(1) / 8

# Subtract the terms to get the result
result = term1 - term2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))