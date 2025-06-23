import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute I_1(2): Modified Bessel function of the first kind of order 1 at 2
bessel_val = mp.besseli(1, 2)

# Multiply by π/4
term1 = mp.pi * bessel_val / 4

# Subtract 1/2
result = term1 - 0.5

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))