import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate pi divided by 4
pi_value = mp.pi
result = pi_value / 4

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))