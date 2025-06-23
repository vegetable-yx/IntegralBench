import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/2
pi_value = mp.pi
result = pi_value / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))