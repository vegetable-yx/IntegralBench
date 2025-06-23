import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the Bessel function of the first kind J0(1)
j0_value = mp.besselj(0, 1)

# Calculate the (1 - J0(1)) component
one_minus_j0 = 1 - j0_value

# Multiply by π to get the final result
result = mp.pi * one_minus_j0

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))