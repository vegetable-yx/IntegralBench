import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute pi/4
pi_over_4 = mp.pi / 4

# Step 2: Compute e^(pi/4)
exp_pi_over_4 = mp.exp(pi_over_4)

# Step 3: Compute square root of 2
sqrt_2 = mp.sqrt(2)

# Step 4: Multiply sqrt(2) by e^(pi/4)
numerator_part = sqrt_2 * exp_pi_over_4

# Step 5: Subtract 1 from the product
numerator = numerator_part - 1

# Step 6: Divide by 2 to get the final result
result = numerator / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))