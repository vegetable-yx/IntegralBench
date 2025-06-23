import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the Bessel function of the first kind J_1(1)
bessel_j1 = mp.besselj(1, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_j1

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))