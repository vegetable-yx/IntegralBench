import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi to the third power
pi_cubed = mp.pi ** 3

# Divide by 192
result = pi_cubed / 192

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))