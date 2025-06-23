import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Step 2: Square the gamma value
gamma_sq = gamma_val ** 2

# Step 3: Compute the denominator: 2 * sqrt(2 * pi)
denom = 2 * mp.sqrt(2 * mp.pi)

# Step 4: Compute the final result
result = gamma_sq / denom

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))