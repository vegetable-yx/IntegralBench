import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: sqrt(2) * Gamma(3/8) * Gamma(7/8) / sqrt(pi)
sqrt2 = mp.sqrt(2)
gamma_3_8 = mp.gamma(3/8)
gamma_7_8 = mp.gamma(7/8)
sqrt_pi = mp.sqrt(mp.pi)

constant_factor = sqrt2 * gamma_3_8 * gamma_7_8 / sqrt_pi

# Calculate the argument for Bessel functions: sqrt(2)/2
arg = mp.sqrt(2) / 2

# Compute modified Bessel functions of the first kind
bessel_minus = mp.besseli(-1/4, arg)  # I_{-1/4}(arg)
bessel_plus = mp.besseli(1/4, arg)    # I_{1/4}(arg)

# Compute the difference: I_{-1/4}(arg) - I_{1/4}(arg)
bessel_diff = bessel_minus - bessel_plus

# Multiply constant factor by Bessel difference to get final result
result = constant_factor * bessel_diff

# Print result to 10 decimal places
print(mp.nstr(result, n=10))