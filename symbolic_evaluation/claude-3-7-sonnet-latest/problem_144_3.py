import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the modified Bessel function of order 0 at 2
bessel_term = mp.besseli(0, 2)

# Compute (1 - I0(2))
one_minus_bessel = 1 - bessel_term

# Multiply by pi/4
result = (mp.pi / 4) * one_minus_bessel

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))