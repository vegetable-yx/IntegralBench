import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate Bessel function of the first kind of order 0 at 1
J0_1 = mp.besselj(0, 1)

# Calculate Bessel function of the first kind of order 1 at 1
J1_1 = mp.besselj(1, 1)

# Compute the difference between the Bessel function values
difference = J0_1 - J1_1

# Multiply the result by pi
result = mp.pi * difference

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))