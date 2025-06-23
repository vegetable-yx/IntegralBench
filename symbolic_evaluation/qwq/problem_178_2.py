import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Bessel function of the first kind of order 4 at 2
j4_2 = mp.besselj(4, 2)

# Multiply by 1/2 to get the final result
result = j4_2 / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))