import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate components separately
sqrt2 = mp.sqrt(2)  # Compute square root of 2
numerator = 5 * sqrt2  # Multiply by coefficient 5
full_expression = numerator * mp.pi  # Multiply by pi
result = full_expression / 8  # Divide by denominator

print(mp.nstr(result, n=10))