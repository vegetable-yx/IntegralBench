import mpmath as mp
mp.dps = 15  # Set internal decimal places for high precision

# Calculate square root of 2 using mpmath
sqrt_2 = mp.sqrt(2)

# Multiply by coefficient 3
three_sqrt2 = 3 * sqrt_2

# Multiply with pi and apply negative sign
result = -three_sqrt2 * mp.pi

# Print final result with exactly 10 decimal places
print(mp.nstr(result, n=10))