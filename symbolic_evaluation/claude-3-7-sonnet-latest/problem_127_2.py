import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: (π * √2) / 2
pi = mp.pi
sqrt2 = mp.sqrt(2)
factor = (pi * sqrt2) / 2

# Calculate the modified Bessel function of the first kind at order 1 and argument 0.5
bessel_val = mp.besseli(1, 0.5)

# Multiply the factor by the Bessel function value
result = factor * bessel_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))