import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Divide π by 2 to get the result
result = pi_value / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))