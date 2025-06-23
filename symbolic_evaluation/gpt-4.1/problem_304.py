import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the complete elliptic integrals at k = 1/2
k_val = mp.mpf(1)/2  # Argument for the elliptic integrals
K_val = mp.ellipk(k_val)  # Complete elliptic integral of the first kind
E_val = mp.ellipe(k_val)  # Complete elliptic integral of the second kind

# Calculate the coefficients and terms
coeff1 = mp.mpf(37)/144  # Coefficient for K(1/2)
term1 = coeff1 * K_val   # First term: (37/144) * K(1/2)

coeff2 = mp.mpf(2)/9     # Coefficient for E(1/2)
term2 = coeff2 * E_val   # Second term: (2/9) * E(1/2)

# Combine the terms to get the result
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))