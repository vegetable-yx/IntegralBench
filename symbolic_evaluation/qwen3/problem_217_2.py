import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate each component separately

# 2 raised to the power of 1/4
term1 = mp.power(2, 0.25)

# Square root of pi
term2 = mp.sqrt(mp.pi)

# Gamma function at 1/4
term3 = mp.gamma(0.25)

# Bessel function of the first kind of order -1/4 evaluated at 1
term4 = mp.besselj(-0.25, 1)

# Multiply all terms together
result = term1 * term2 * term3 * term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))