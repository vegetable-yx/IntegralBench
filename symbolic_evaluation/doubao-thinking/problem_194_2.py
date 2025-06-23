import mpmath as mp

# Set internal decimal places for calculations
mp.dps = 15

# Compute pi constant
pi_val = mp.pi

# Compute complete elliptic integral of the first kind K(1/2)
k_half = mp.ellipk(0.5)

# Compute complete elliptic integral of the second kind E(1/2)
e_half = mp.ellipe(0.5)

# Calculate each term in the expression
term1 = -pi_val
term2 = 4 * e_half
term3 = -(3/2) * k_half

# Combine terms to get the final result
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))