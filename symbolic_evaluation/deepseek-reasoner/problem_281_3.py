import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the constant term (pi * sqrt(2)) / 2
constant_term = (mp.pi * mp.sqrt(2)) / 2

# Compute exponential term e^4
exp_term = mp.exp(4)

# Compute modified Bessel functions of the first kind
bessel_plus_14 = mp.besseli(0.25, 4)
bessel_minus_14 = mp.besseli(-0.25, 4)

# Combine all components to get final result
result = constant_term * exp_term * bessel_plus_14 * bessel_minus_14

# Print result with 10 decimal places
print(mp.nstr(result, n=10))