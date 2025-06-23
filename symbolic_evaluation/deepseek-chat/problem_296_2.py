import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modulus squared: m = (1/sqrt(2))^2 = 0.5
m = (1 / mp.sqrt(2))**2

# Compute the complete elliptic integral of the second kind E(m)
E_val = mp.ellipe(m)

# Square the elliptic integral value
E_squared = E_val**2

# Multiply by pi/8 to get the final result
result = (mp.pi / 8) * E_squared

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))