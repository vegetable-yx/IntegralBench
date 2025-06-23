import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the constant factor: sqrt(pi/2)
factor = mp.sqrt(mp.pi / 2)

# Compute the exponential factor: exp(-1/2)
exp_factor = mp.exp(-0.5)

# Compute the modified Bessel functions at z = 1/2
# I_{-1/4}(1/2)
bessel_minus = mp.besseli(-0.25, 0.5)
# I_{1/4}(1/2)
bessel_plus = mp.besseli(0.25, 0.5)

# Sum the Bessel functions
bessel_sum = bessel_minus + bessel_plus

# Combine all factors: sqrt(pi/2) * exp(-1/2) * [I_{-1/4}(1/2) + I_{1/4}(1/2)]
result = factor * exp_factor * bessel_sum

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))