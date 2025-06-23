import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π using mpmath's built-in constant
pi_value = mp.pi

# Divide π by 2 to get the result
result = pi_value / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))