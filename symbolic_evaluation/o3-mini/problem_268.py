import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Compute the value of pi
pi_val = mp.pi

# Compute zeta(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Multiply pi and zeta(3)
pi_zeta3 = pi_val * zeta3

# Divide the product by 8 to get the final result
result = pi_zeta3 / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))