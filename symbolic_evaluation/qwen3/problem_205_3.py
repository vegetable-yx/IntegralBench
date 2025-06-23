import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the Bessel function of the first kind of order 1 at 1
j1_value = mp.besselj(1, 1)

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply the results to get the final value
result = sqrt2 * j1_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))