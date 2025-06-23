import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Bessel function of the first kind of order 0 at 1
j0_1 = mp.besselj(0, 1)

# Calculate Bessel function of the first kind of order 1 at 1
j1_1 = mp.besselj(1, 1)

# Compute the difference between the Bessel function values
difference = j0_1 - j1_1

# Multiply by π to get the final result
result = mp.pi * difference

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))