import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the constant terms: sqrt(pi) and exp(1/2)
sqrt_pi = mp.sqrt(mp.pi)
exp_half = mp.exp(0.5)

# Combine constant numerator: sqrt(pi) * e^(1/2)
numerator = sqrt_pi * exp_half

# Compute the denominator: sqrt(2)
denominator = mp.sqrt(2)

# Compute the Bessel function terms at x = 1/2
bessel_minus = mp.besseli(-0.25, 0.5)  # I_{-1/4}(1/2)
bessel_plus = mp.besseli(0.25, 0.5)    # I_{1/4}(1/2)

# Compute the difference: I_{-1/4}(1/2) - I_{1/4}(1/2)
bessel_diff = bessel_minus - bessel_plus

# Combine all parts: [sqrt(pi) * e^{1/2} / sqrt(2)] * [bessel_diff]
result = (numerator / denominator) * bessel_diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))