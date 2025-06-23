import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Compute pi cubed
pi_cubed = mp.pi ** 3

# Divide by 48 to get the result
result = pi_cubed / 48

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))