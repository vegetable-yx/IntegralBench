import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Multiply by 2
two_sqrt_two = 2 * sqrt_two

# Multiply by pi to get the final result
result = two_sqrt_two * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))