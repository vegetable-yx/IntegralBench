import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi cubed
pi_cubed = mp.pi ** 3

# Divide by 48 to get the final result
result = pi_cubed / 48

# Output the result to 10 decimal places
print(mp.nstr(result, n=10))