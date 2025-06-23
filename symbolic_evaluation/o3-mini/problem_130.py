import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the constant sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Compute e^(1/4)
exp_term = mp.exp(1/4)

# Multiply sqrt(pi) and e^(1/4) to form the first factor
factor1 = sqrt_pi * exp_term

# Compute the modified Bessel functions I_{-1/4}(1/4) and I_{1/4}(1/4)
bessel_neg = mp.besseli(-1/4, 1/4)
bessel_pos = mp.besseli(1/4, 1/4)

# Compute the difference: I_{-1/4}(1/4) - I_{1/4}(1/4)
bessel_diff = bessel_neg - bessel_pos

# Multiply the first factor by the Bessel difference to get the result
result = factor1 * bessel_diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))