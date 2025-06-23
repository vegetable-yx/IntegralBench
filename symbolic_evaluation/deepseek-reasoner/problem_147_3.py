import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply components and divide by 2
result = (sqrt2 * pi_squared) / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))