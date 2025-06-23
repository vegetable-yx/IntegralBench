import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 2 to get final result
result = pi_squared / 2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))