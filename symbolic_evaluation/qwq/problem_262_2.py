import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the Bessel function of the first kind of order 0 at 2
j0_2 = mp.besselj(0, 2)

# Calculate the numerator (1 - J0(2))
numerator = 1 - j0_2

# Divide by 4 to get the final result
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))