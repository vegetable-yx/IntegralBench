import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (example values, user can modify)
a = 1.0
b = 1.0

# Compute Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(3/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Multiply Gamma functions
gamma_product = gamma_14 * gamma_34

# Calculate argument for hypergeometric function: (b^2 * a^2)/4
arg = (b**2 * a**2) / 4

# Compute confluent hypergeometric function {}_1F_1(1/2; 1; arg)
hyp_val = mp.hyp1f1(mp.mpf(1)/2, 1, arg)

# Combine results
result = gamma_product * hyp_val

# Print final result with 10 decimal places
print(mp.nstr(result, n=10))