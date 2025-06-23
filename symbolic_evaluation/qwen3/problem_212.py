import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Bessel functions of the first kind at x=1
j0 = mp.besselj(0, 1)  # J_0(1)
j1 = mp.besselj(1, 1)  # J_1(1)

# Calculate the difference between Bessel functions
diff_bessel = j0 - j1

# Multiply by pi to get the final result
result = mp.pi * diff_bessel

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))