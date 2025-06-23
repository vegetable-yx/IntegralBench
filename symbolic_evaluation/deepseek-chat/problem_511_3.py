import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Step 2: Multiply by 2 to get the argument for sine
arg = 2 * sqrt2

# Step 3: Compute the sine of the argument
sin_val = mp.sin(arg)

# Step 4: Multiply the sine result by 2 to get the final answer
result = 2 * sin_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))