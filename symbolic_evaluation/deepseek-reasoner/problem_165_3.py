import mpmath as mp
mp.dps = 15

# Compute the modified Bessel function of first kind I0 at 2
bessel_i0 = mp.besseli(0, 2)

# Compute the exponential term e^(-2)
exp_term = mp.exp(-2)

# Calculate the product of Bessel function and exponential
bessel_exp_product = bessel_i0 * exp_term

# Compute the (1 - product) term
parenthetical_term = 1 - bessel_exp_product

# Multiply by pi/2 to get final result
result = (mp.pi / 2) * parenthetical_term

print(mp.nstr(result, n=10))