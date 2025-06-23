import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Bessel function of the first kind of order 0 at 1
j0_value = mp.besselj(0, 1)

# Multiply by pi to get the final result
result = mp.pi * j0_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))