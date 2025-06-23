import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi divided by 2
pi_over_2 = mp.pi / 2

# Compute square root of (pi/2)
result = mp.sqrt(pi_over_2)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))