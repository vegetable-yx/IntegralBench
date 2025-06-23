import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Bessel function values at x = 1/2
# J_{-1/4}(1/2)
bessel_minus_quarter = mp.besselj(-0.25, 0.5)

# J_{1/4}(1/2)
bessel_quarter = mp.besselj(0.25, 0.5)

# Compute the difference between the Bessel functions
bessel_diff = bessel_minus_quarter - bessel_quarter

# Calculate the constant factor: (π * √2) / 2
constant_factor = (mp.pi * mp.sqrt(2)) / 2

# Multiply the constant factor by the Bessel difference
result = constant_factor * bessel_diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))