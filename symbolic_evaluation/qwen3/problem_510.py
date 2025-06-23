import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the denominator 3*sqrt(3)
denominator = 3 * sqrt3

# Calculate the coefficient 7 divided by the denominator
coefficient = 7 / denominator

# Multiply by pi to get the final result
result = coefficient * mp.pi

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))