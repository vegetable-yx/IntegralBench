import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the argument for the elliptic integral: k = 1/sqrt(2)
k = mp.one / mp.sqrt(2)

# Evaluate the complete elliptic integral of the first kind K(k)
ellip_val = mp.ellipk(k)

# Compute the constant factor: (1/2) * pi * sqrt(2)
constant_factor = mp.one/2 * mp.pi * mp.sqrt(2)

# Multiply the constant factor by the elliptic integral value
result = constant_factor * ellip_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))