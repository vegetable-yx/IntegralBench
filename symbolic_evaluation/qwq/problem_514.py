import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Calculate the first term: π/6
term1 = pi_val / 6

# Calculate the second term: sqrt(3)/8
sqrt3 = mp.sqrt(3)
term2 = sqrt3 / 8

# Sum both terms to get final result
result = term1 + term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))