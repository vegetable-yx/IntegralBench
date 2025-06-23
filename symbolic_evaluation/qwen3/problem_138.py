import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate I_0(6) using the modified Bessel function of the first kind
i0 = mp.besseli(0, 6)

# Subtract 1 from the Bessel function result
numerator = i0 - 1

# Divide by 3 to get the final result
result = numerator / 3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))