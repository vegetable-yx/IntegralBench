import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Compute the exponent: e^(1/8)
exp_term = mp.exp(mp.mpf(1)/8)

# Compute the square root term: sqrt(pi/2)
sqrt_term = mp.sqrt(mp.pi / 2)

# Multiply the two terms to get the final result
result = exp_term * sqrt_term

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))