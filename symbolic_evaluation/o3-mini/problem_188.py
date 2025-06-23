import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Step 1: Compute the constant expression: 13 + sqrt(168)
base = 13 + mp.sqrt(168)

# Step 2: Compute the parameter t = 1 / (13 + sqrt(168))
t = 1 / base

# Step 3: Compute the argument for the first Gamma function: 1/2 + t
gamma_arg1 = mp.mpf('0.5') + t

# Step 4: Compute the argument for the second Gamma function: 1 + t
gamma_arg2 = 1 + t

# Step 5: Calculate Gamma(1/2 + t)
gamma1 = mp.gamma(gamma_arg1)

# Step 6: Calculate Gamma(1 + t)
gamma2 = mp.gamma(gamma_arg2)

# Step 7: Compute the hypergeometric function _2F_1(1/2, t; 1 + t; -1)
hyp2f1_val = mp.hyp2f1(mp.mpf('0.5'), t, gamma_arg2, -1)

# Step 8: Compute the numerator: sqrt(pi) * Gamma(1/2 + t)
numerator = mp.sqrt(mp.pi) * gamma1

# Step 9: Compute the denominator: 4 * (13 + sqrt(168)) * Gamma(1 + t)
denominator = 4 * base * gamma2

# Step 10: Combine to get the final result: numerator / denominator * hyp2f1_val
result = (numerator / denominator) * hyp2f1_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))