import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi/4
pi_val = mp.pi
result = pi_val / 4

# Print result to 10 decimal places
print(mp.nstr(result, n=10))