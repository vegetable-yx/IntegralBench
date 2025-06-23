import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Step 1: Calculate pi divided by 2
pi_over_2 = mp.pi / 2

# Step 2: Compute the square root of (pi/2)
sqrt_pi_over_2 = mp.sqrt(pi_over_2)

# Step 3: Calculate the exponent 1/8
exponent = mp.mpf(1) / 8

# Step 4: Compute e raised to the power of 1/8
exp_term = mp.exp(exponent)

# Step 5: Multiply the two components together
result = sqrt_pi_over_2 * exp_term

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))