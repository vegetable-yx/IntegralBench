import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Bessel function of the first kind of order 1 at 1
j1_value = mp.besselj(1, 1)

# Multiply by π to get the final result
result = mp.pi * j1_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))