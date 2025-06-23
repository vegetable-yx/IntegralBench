import mpmath as mp

# Set internal decimal precision to 15 digits for calculations
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Subtract 1 from sqrt(2)
sqrt_minus_one = sqrt2 - 1

# Multiply the result by pi
result = mp.pi * sqrt_minus_one

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))