import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the argument for the Bessel functions
x = mp.mpf('0.25')

# Calculate Bessel functions of the first kind for orders -1/4 and 1/4
j_neg_quarter = mp.besselj(-0.25, x)
j_quarter = mp.besselj(0.25, x)

# Compute the difference between the two Bessel functions
diff_bessel = j_neg_quarter - j_quarter

# Multiply by sqrt(2) * pi
result = mp.sqrt(2) * mp.pi * diff_bessel

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))