import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Step 1: Calculate the square root of 2
sqrt_val = mp.sqrt(2)

# Step 2: Multiply the square root by 2
inner_arg = 2 * sqrt_val

# Step 3: Compute the sine of the inner argument
sin_val = mp.sin(inner_arg)

# Step 4: Multiply the sine result by 2
result = 2 * sin_val

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))