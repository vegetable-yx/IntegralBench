import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Step 1: Calculate the square root of 2
sqrt_val = mp.sqrt(2)

# Step 2: Multiply by 2 to get the argument for sine
angle = 2 * sqrt_val

# Step 3: Compute the sine of the angle
sin_val = mp.sin(angle)

# Step 4: Multiply by 2 to get the final result
result = 2 * sin_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))