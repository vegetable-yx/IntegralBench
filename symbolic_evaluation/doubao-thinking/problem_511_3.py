import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute square root of 2
sqrt_val = mp.sqrt(2)

# Step 2: Multiply by 2 to get the argument for sine
arg = 2 * sqrt_val

# Step 3: Compute sine of the argument
sin_val = mp.sin(arg)

# Step 4: Multiply sine result by 2
result = 2 * sin_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))