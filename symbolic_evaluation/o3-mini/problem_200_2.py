import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the argument for the Bessel functions: 1/sqrt(2)
x = 1 / mp.sqrt(2)

# Compute Bessel functions of the first kind at orders -1/4 and 1/4
j_minus_quarter = mp.besselj(-1/4, x)
j_quarter = mp.besselj(1/4, x)

# Square the Bessel function values
j_minus_quarter_sq = j_minus_quarter ** 2
j_quarter_sq = j_quarter ** 2

# Compute the difference of squares
diff_sq = j_minus_quarter_sq - j_quarter_sq

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * diff_sq

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))