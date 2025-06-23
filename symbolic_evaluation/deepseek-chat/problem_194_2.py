import mpmath as mp

# Set internal decimal precision to 15 digits for calculations
mp.dps = 15

# Calculate pi divided by 8
pi_value = mp.pi
result = pi_value / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))