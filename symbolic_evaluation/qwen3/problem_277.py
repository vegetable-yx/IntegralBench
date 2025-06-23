import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute the modified Bessel function of the first kind of order 1 at 1
i1_value = mp.besseli(1, 1)

# Multiply by π to get the final result
result = mp.pi * i1_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))