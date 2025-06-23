import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute modified Bessel function of the first kind of order 1 at 2
i1_value = mp.besseli(1, 2)

# Square the Bessel function result
i1_squared = i1_value ** 2

# Multiply by 2 to get the final result
result = 2 * i1_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))