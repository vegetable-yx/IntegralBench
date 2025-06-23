import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Step 1: Calculate the square root of 2
sqrt_val = mp.sqrt(2)

# Step 2: Multiply by 2 to form the argument for sine
arg = 2 * sqrt_val

# Step 3: Compute the sine of the argument
sin_val = mp.sin(arg)

# Step 4: Multiply by 2 to get the final result
result = 2 * sin_val

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))