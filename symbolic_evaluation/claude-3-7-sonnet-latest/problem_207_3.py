import mpmath as mp

# Set decimal places for internal calculations to 15
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply pi squared by sqrt(2)
numerator = pi_sq * sqrt_2

# Divide by 8 to get the final result
result = numerator / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))