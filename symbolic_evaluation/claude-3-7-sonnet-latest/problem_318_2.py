import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute π using mpmath constant
pi_val = mp.pi

# Divide π by 8 to get the result
result = pi_val / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))