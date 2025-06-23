import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute components of the expression
# Step 1: Calculate sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Step 2: Compute gamma functions
gamma_34 = mp.gamma(mp.mpf(3)/4)   # Gamma(3/4)
gamma_54 = mp.gamma(mp.mpf(5)/4)   # Gamma(5/4)

# Step 3: Compute the coefficient fraction: (sqrt(pi) * Gamma(3/4)) / (2 * Gamma(5/4))
coeff = (sqrt_pi * gamma_34) / (2 * gamma_54)

# Step 4: Evaluate the hypergeometric function 2F1(-1/4, 1/2; 5/4; 1/16)
hyp_val = mp.hyp2f1(mp.mpf(-1)/4, mp.mpf(1)/2, mp.mpf(5)/4, mp.mpf(1)/16)

# Step 5: Multiply coefficient by hypergeometric value
result = coeff * hyp_val

# Print final result with 10 decimal places
print(mp.nstr(result, n=10))