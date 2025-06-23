import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute arctan(1/sqrt(3))
atan_val = mp.atan(1 / sqrt3)

# Add pi to the arctan result
sum_val = mp.pi + atan_val

# Multiply by 2/sqrt(3)
result = (2 / sqrt3) * sum_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))