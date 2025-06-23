import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the value for 'a'
a = 1.0

# Compute Bessel function of the first kind of order 1 at a
bessel_j1 = mp.besselj(1, a)

# Compute Struve function of order 1 at a
struve_h1 = mp.struveh(1, a)

# Compute the expression: J_1(a) - H_1(a)
result = bessel_j1 - struve_h1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))