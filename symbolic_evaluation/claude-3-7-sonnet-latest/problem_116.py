import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^3
pi_cubed = mp.pi ** 3

# Denominator is 24
denominator = 24

# Compute the result: pi^3 / 24
result = pi_cubed / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))