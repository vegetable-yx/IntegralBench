import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Bessel function of the first kind of order 0 at 1
j0 = mp.besselj(0, 1)

# Calculate modified Struve function of order 0 at 1
l0 = mp.struvel(0, 1)

# Compute the difference between Bessel and Struve functions
difference = j0 - l0

# Multiply by pi to get the final result
result = mp.pi * difference

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))