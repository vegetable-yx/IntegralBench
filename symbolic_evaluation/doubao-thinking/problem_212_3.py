import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Bessel function of the first kind of order 0 at 1
j0_val = mp.besselj(0, 1)

# Compute Bessel function of the first kind of order 2 at 1
j2_val = mp.besselj(2, 1)

# Calculate the difference between the Bessel function values
difference = j0_val - j2_val

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * difference

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))