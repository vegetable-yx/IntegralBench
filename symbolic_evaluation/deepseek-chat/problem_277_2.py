import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 1 at 1
bessel_i1 = mp.besseli(1, 1)

# Compute the modified Struve function of order 1 at 1
struve_l1 = mp.struvel(1, 1)

# Sum the two function values
sum_functions = bessel_i1 + struve_l1

# Multiply by pi/2
result = (mp.pi / 2) * sum_functions

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))