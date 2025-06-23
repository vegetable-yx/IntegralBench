import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate pi to the fourth power
pi_4 = mp.pi**4

# Divide by 120 to get the result
result = pi_4 / 120

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))