import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/4
pi_constant = mp.pi
result = pi_constant / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))