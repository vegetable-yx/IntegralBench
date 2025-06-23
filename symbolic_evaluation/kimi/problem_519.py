import mpmath as mp

# Set internal decimal precision to 15 for sufficient accuracy
mp.dps = 15

# Compute π using mpmath constant
pi_val = mp.pi

# Divide π by 4 to obtain the result
result = pi_val / 4

# Print the final result formatted to 10 decimal places
print(mp.nstr(result, n=10))