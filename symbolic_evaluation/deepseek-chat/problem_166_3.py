import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi/4 directly
pi_val = mp.pi
result = pi_val / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))