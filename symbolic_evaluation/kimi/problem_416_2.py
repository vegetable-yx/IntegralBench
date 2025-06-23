import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Step 1: Compute π/4
pi_over_4 = mp.pi / 4

# Step 2: Compute e^(π/4)
exp_pi_over_4 = mp.exp(pi_over_4)

# Step 3: Compute the square root of 2
sqrt_2 = mp.sqrt(2)

# Step 4: Multiply e^(π/4) by √2
numerator_part = exp_pi_over_4 * sqrt_2

# Step 5: Subtract 1 from the product
adjusted_numerator = numerator_part - 1

# Step 6: Divide by 2 to get the final result
result = adjusted_numerator / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))