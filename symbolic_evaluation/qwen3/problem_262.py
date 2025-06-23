import mpmath as mp

mp.dps = 15  # Set internal precision

# Define the parameter 'a' - replace value as needed
a = mp.mpf('1.0')

# Calculate Bessel function of first kind J1(a)
j1_value = mp.besselj(1, a)

# Calculate numerator: π * J1(a)
numerator = mp.pi * j1_value

# Calculate denominator: 4a
denominator = 4 * a

# Compute final result
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))