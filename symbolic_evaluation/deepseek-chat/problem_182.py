import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute pi constant using mpmath
pi_value = mp.pi

# Divide pi by 2 to get the result
result = pi_value / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))