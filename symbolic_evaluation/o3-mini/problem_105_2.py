import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the argument for the elliptic integral: phi = pi/6
phi = mp.pi / 6

# Compute the incomplete elliptic integral of the second kind E(phi, m)
# Here m = k^2 = 2^2 = 4
E_val = mp.ellipe(phi, 4)

# Multiply by 2 as per the expression
result = 2 * E_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))