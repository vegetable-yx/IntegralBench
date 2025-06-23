import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Subtract 1 from sqrt(2)
sqrt_two_minus_one = sqrt_two - 1

# Multiply by pi
result = mp.pi * sqrt_two_minus_one

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))