import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant factor: denominator = 2^(5/4) * Gamma(3/4)
# First, compute 2^(5/4)
two_power = mp.power(2, mp.mpf(5)/4)

# Compute Gamma(3/4)
gamma_val = mp.gamma(mp.mpf(3)/4)

# Combine denominator: two_power * gamma_val
denominator = two_power * gamma_val

# Numerator is pi
numerator = mp.pi

# Compute the multiplicative factor: pi / denominator
factor = numerator / denominator

# Compute the modified Bessel functions of the first kind
# I_{-1/4}(1/2) and I_{1/4}(1/2)
bessel_minus = mp.besseli(mp.mpf(-1)/4, mp.mpf(1)/2)
bessel_plus = mp.besseli(mp.mpf(1)/4, mp.mpf(1)/2)

# Compute the difference: I_{-1/4}(1/2) - I_{1/4}(1/2)
diff = bessel_minus - bessel_plus

# Multiply by the factor to get the final result
result = factor * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))