import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate pi cubed: π^3
pi_cubed = mp.pi ** 3

# Divide by 16 to obtain the result
result = pi_cubed / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))