import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Multiply by pi to get the final result
result = sqrt_two * mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))