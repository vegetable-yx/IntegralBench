import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi ** 2

# Divide by 8
div_result = pi_sq / 8

# Apply negative sign
result = -div_result

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))