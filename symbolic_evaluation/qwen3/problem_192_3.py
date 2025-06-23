import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi to the fourth power
pi_4 = mp.pi ** 4

# Divide by 96
result = pi_4 / 96

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))