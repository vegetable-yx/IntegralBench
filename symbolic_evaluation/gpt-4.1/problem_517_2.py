import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the exponent term: e^(1/8)
exponent_term = mp.exp(1/8)

# Calculate the square root term: sqrt(pi/2)
# First compute pi/2
pi_over_2 = mp.pi / 2
# Then take square root
sqrt_term = mp.sqrt(pi_over_2)

# Multiply the two components
result = exponent_term * sqrt_term

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))