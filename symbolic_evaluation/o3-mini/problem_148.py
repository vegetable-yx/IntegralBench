import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Step 1: Compute gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Step 2: Raise gamma(1/4) to the 4th power
gamma_fourth = gamma_val**4

# Step 3: Compute sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Step 4: Compute denominator: 32 * sqrt(pi)
denominator = 32 * sqrt_pi

# Step 5: Compute the final result: gamma(1/4)^4 / (32 * sqrt(pi))
result = gamma_fourth / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))