import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 16
denominator = 16
fraction = pi_squared / denominator

# Apply the negative sign
result = -fraction

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))