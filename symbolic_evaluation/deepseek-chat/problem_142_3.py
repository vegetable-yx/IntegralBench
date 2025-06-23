import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Compute the value of the modified Bessel function of the first kind of order 0 at 1
i0_val = mp.besseli(0, 1)

# Compute the value of the modified Bessel function of the first kind of order 1 at 1
i1_val = mp.besseli(1, 1)

# Square the Bessel function values
i0_sq = i0_val ** 2
i1_sq = i1_val ** 2

# Compute the difference of the squares
diff_sq = i0_sq - i1_sq

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * diff_sq

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))