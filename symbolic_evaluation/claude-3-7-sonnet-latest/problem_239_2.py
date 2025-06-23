import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at 2
I0 = mp.besseli(0, 2)

# Compute the modified Bessel function of the second kind of order 0 at 2
K0 = mp.besselk(0, 2)

# Calculate the expression: K0(2) * (I0(2) - 1)
result = K0 * (I0 - 1)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))