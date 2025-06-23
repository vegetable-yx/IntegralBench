import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute e^(1/8)
exp_part = mp.exp(1/8)

# Step 2: Compute π
pi_val = mp.pi

# Step 3: Compute π/2
pi_over_2 = pi_val / 2

# Step 4: Compute sqrt(π/2)
sqrt_part = mp.sqrt(pi_over_2)

# Step 5: Multiply the two parts: e^(1/8) * sqrt(π/2)
result = exp_part * sqrt_part

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))