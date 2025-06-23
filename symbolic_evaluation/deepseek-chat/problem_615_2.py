import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute the constant sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate the expression inside the cube roots: 7 + 5*sqrt(2)
a = 7 + 5 * sqrt2

# Compute the cube root of a
a_cbrt = mp.power(a, mp.mpf(1)/3)

# Compute the inverse cube root of a (i.e., a^(-1/3))
a_inv_cbrt = 1 / a_cbrt

# Calculate the average: (a_cbrt + a_inv_cbrt) / 2
avg = (a_cbrt + a_inv_cbrt) / 2

# Subtract 1 and multiply by 3
result = 3 * (avg - 1)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))