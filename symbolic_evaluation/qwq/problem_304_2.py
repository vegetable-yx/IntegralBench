import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate 3 times square root of 3
sqrt3 = mp.sqrt(3)
three_sqrt3 = 3 * sqrt3

# Compute numerator (π² - 3√3)
numerator = pi_squared - three_sqrt3

# Divide by 48 to get final result
result = numerator / 48

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))