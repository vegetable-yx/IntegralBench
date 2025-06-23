import mpmath as mp
mp.dps = 15

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute Beta function B(3/4, 1/4)
beta_value = mp.beta(3/4, 1/4)

# Compute modified Bessel function I_{-1/2}(1)
bessel_value = mp.besseli(-0.5, 1)

# Combine all components
result = sqrt2 * beta_value * bessel_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))