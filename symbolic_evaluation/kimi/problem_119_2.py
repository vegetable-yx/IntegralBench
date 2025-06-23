import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the factor (2 - sqrt(2))
factor = 2 - sqrt2

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply pi squared by the factor
numerator = pi_squared * factor

# Divide by 6 to get the final result
result = numerator / 6

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))