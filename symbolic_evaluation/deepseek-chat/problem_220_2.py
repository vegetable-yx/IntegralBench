import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by pi to get the result
result = mp.pi * sqrt_2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))