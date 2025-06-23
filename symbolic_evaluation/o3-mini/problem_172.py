import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant factor: sqrt(pi) * Gamma(3/4) / (128 * Gamma(5/4))
# Step 1: Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(3/4)

# Step 2: Calculate Gamma(5/4)
gamma_5_4 = mp.gamma(5/4)

# Step 3: Compute the denominator: 128 * Gamma(5/4)
denominator = 128 * gamma_5_4

# Step 4: Compute numerator: sqrt(pi) * Gamma(3/4)
numerator = mp.sqrt(mp.pi) * gamma_3_4

# Step 5: Compute the constant factor
constant_factor = numerator / denominator

# Compute the hypergeometric function _3F_2([1/2, 1, 1], [3/4, 5/4], 1)
# Arguments: a = [0.5, 1, 1], b = [0.75, 1.25], z = 1
hyp = mp.hyper([0.5, 1, 1], [3/4, 5/4], 1)

# Multiply the constant factor by the hypergeometric result
result = constant_factor * hyp

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))