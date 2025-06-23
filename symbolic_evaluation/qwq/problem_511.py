import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by 2 to get 2*sqrt(2)
two_sqrt2 = 2 * sqrt_2

# Compute the sine of 2*sqrt(2)
sin_term = mp.sin(two_sqrt2)

# Multiply by 2 to get the final result
result = 2 * sin_term

print(mp.nstr(result, n=10))