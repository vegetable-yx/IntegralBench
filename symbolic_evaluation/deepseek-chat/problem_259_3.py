import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute the Struve function of order 0 at x=1
struve_value = mp.struveh(0, 1)

# Compute the Bessel function of the second kind of order 0 at x=1
besselY_value = mp.bessely(0, 1)

# Combine the special functions: H_0(1) - Y_0(1)
special_diff = struve_value - besselY_value

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * special_diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))