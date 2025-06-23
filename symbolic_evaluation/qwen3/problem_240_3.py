import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Calculate 2 times sqrt(2)
denominator = 2 * sqrt_2

# Compute the final result as reciprocal of the denominator
result = 1 / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))