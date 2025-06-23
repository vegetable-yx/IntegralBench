import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute I_0(1) - modified Bessel function of the first kind, order 0 at 1
bessel_i0 = mp.besseli(0, 1)

# Compute I_1(1) - modified Bessel function of the first kind, order 1 at 1
bessel_i1 = mp.besseli(1, 1)

# Compute the difference: I_0(1) - I_1(1)
diff = bessel_i0 - bessel_i1

# Multiply by pi/2
result = (mp.pi / 2) * diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))