import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate π using mpmath
pi_val = mp.pi

# Divide π by 3 to get the result
result = pi_val / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))