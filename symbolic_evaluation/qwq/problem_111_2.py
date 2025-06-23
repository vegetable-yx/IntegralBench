import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute (π² - 8)
pi_squared_minus_8 = pi_squared - 8

# Multiply by √2 to get final result
result = mp.sqrt(2) * pi_squared_minus_8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))