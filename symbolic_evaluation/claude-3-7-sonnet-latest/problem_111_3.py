import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Multiply pi squared by the square root of 2
numerator = pi_squared * sqrt_two

# Divide by 3 to get the final result
result = numerator / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))