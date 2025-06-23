import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Step 2: Raise Gamma(1/4) to the 8th power
gamma_power = gamma_val**8

# Step 3: Compute pi squared
pi_sq = mp.pi**2

# Step 4: Calculate the denominator: 1024 * pi^2
denominator = 1024 * pi_sq

# Step 5: Compute the fraction: Gamma(1/4)^8 / (1024 * pi^2)
fraction = gamma_power / denominator

# Step 6: Add 1/8 to the fraction
result = fraction + mp.mpf(1)/8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))