import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Bessel function of first kind at order 0
j0_val = mp.besselj(0, 2)

# Calculate Bessel function of first kind at order 2
j2_val = mp.besselj(2, 2)

# Compute the average of the two Bessel function values
result = 0.5 * (j0_val + j2_val)

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))