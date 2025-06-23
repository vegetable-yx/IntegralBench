import mpmath as mp

# Set the precision for internal calculations
mp.dps = 15

# Define the constant
a = mp.mpf('2.0')

# Calculate the result using the analytical expression
# Result = 2 * (sqrt(2) * (3*E(1/2) - K(1/2)) / (3*sqrt(pi)))
# Where E and K are complete elliptic integrals

# Compute the argument k = 1/sqrt(2)
k = 1 / mp.sqrt(2)

# Calculate complete elliptic integrals E(k) and K(k)
E_k = mp.ellipe(k)
K_k = mp.ellipk(k)

# Numerator: 3*E_k - K_k
numerator = 3 * E_k - K_k

# Denominator: 3 * sqrt(pi)
denominator = 3 * mp.sqrt(mp.pi)

# Multiply by sqrt(2)
factor = mp.sqrt(2)

# Combine: factor * numerator / denominator
result = 2 * (factor * numerator) / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))