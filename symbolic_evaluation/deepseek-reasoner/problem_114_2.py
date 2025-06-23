import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi constant
pi_value = mp.pi

# Compute the final result using exact analytical expression
result = -pi_value / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))