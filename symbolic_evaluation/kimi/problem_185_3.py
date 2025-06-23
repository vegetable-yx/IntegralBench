import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the square root of 8
sqrt_8 = mp.sqrt(8)

# Calculate the denominator component (3 + sqrt(8))
denominator_component = 3 + sqrt_8

# Multiply by 16 to get the full denominator
full_denominator = 16 * denominator_component

# Calculate the numerator (pi squared)
pi_squared = mp.pi ** 2

# Compute the final result by dividing numerator by denominator
result = pi_squared / full_denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))