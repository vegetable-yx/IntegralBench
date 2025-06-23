import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the Bessel function of the first kind of order 0 at 2
bessel_value = mp.besselj(0, 2)

# Compute 1 minus the Bessel value
one_minus_bessel = 1 - bessel_value

# Multiply by pi
numerator = mp.pi * one_minus_bessel

# Divide by 8 to get the final result
result = numerator / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))