import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^3
pi_cubed = mp.pi ** 3

# Compute first term: pi^3 / 192
term1 = pi_cubed / 192

# Compute second term: pi / 64
term2 = mp.pi / 64

# Calculate final result by subtracting terms
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))