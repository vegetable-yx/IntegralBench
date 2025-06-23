import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate sqrt(2) and divide by 2
sqrt2_over_2 = mp.sqrt(2) / 2

# Compute hyperbolic sine of sqrt(2)/2
sinh_value = mp.sinh(sqrt2_over_2)

# Multiply by 4 to get final result
result = 4 * sinh_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))