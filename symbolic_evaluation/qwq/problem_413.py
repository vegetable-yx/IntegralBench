import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate 506 * π using high-precision arithmetic
coefficient = 506
exact_value = coefficient * mp.pi

# Convert to decimal with exactly 10 decimal places
print(mp.nstr(exact_value, n=10))