import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute e^(1/2)
exp_half = mp.exp(0.5)

# Compute the modified Bessel function of the second kind K_{1/4}(1/2)
bessel_val = mp.besselk(0.25, 0.5)

# Numerator: 2 * e^{1/2} * K_{1/4}(1/2)
numerator = 2 * exp_half * bessel_val

# Denominator: π
denominator = mp.pi

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))