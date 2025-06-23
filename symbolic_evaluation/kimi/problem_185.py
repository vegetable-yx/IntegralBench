import mpmath as mp
mp.dps = 15

# Compute square root of 8
sqrt_8 = mp.sqrt(8)

# Calculate denominator base (3 + sqrt(8))
denominator_base = 3 + sqrt_8

# Multiply by 16 to get full denominator
full_denominator = 16 * denominator_base

# Compute pi squared
pi_squared = mp.pi ** 2

# Calculate the result
result = pi_squared / full_denominator

# Print with 10 decimal precision
print(mp.nstr(result, n=10))