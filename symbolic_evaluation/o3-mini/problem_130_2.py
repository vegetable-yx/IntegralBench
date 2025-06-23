import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the constant factor: sqrt(2 * pi)
factor1 = mp.sqrt(2 * mp.pi)

# Compute e^(1/2)
factor2 = mp.exp(0.5)

# Compute the modified Bessel functions at z = 1/2
# I_{-1/4}(1/2)
bessel_minus = mp.besseli(-0.25, 0.5)

# I_{1/4}(1/2)
bessel_plus = mp.besseli(0.25, 0.5)

# Compute the difference: I_{-1/4}(1/2) - I_{1/4}(1/2)
bessel_diff = bessel_minus - bessel_plus

# Multiply all factors together: sqrt(2*pi) * e^(1/2) * (bessel_diff)
result = factor1 * factor2 * bessel_diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))