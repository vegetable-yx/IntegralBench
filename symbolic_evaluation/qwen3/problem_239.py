import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate modified Bessel function of the first kind I_0 at 2
i0_2 = mp.besseli(0, 2)

# Calculate modified Bessel function of the second kind K_0 at 2
k0_2 = mp.besselk(0, 2)

# Compute the final result using the analytical expression
result = i0_2 - k0_2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))