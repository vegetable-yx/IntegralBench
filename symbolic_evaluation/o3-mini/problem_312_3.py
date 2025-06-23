import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi^(3/2)
pi_sqrt = mp.sqrt(mp.pi)
pi_power = pi_sqrt * mp.pi  # pi^(3/2) = pi * sqrt(pi)

# Compute the exponential factor: exp(-1/4)
exp_factor = mp.exp(-0.25)

# Evaluate the modified Bessel functions at x = 1/4
bessel_minus = mp.besseli(-0.25, 0.25)  # I_{-1/4}(1/4)
bessel_plus = mp.besseli(0.25, 0.25)    # I_{1/4}(1/4)
bessel_sum = bessel_minus + bessel_plus

# Calculate the first term: (pi^(3/2)/8 * exp(-1/4) * [bessel_sum]
term1 = (pi_power / 8) * exp_factor * bessel_sum

# Compute the complementary error function: erfc(1/2)
erfc_val = mp.erfc(0.5)

# Calculate the second term: (pi/4) * erfc(1/2)
term2 = (mp.pi / 4) * erfc_val

# Combine terms: I = term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))