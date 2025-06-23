import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt_2 = mp.sqrt(2)

# Step 2: Multiply pi by the square root of 2
pi_times_sqrt2 = mp.pi * sqrt_2

# Step 3: Divide the product by 2 to obtain the final result
result = pi_times_sqrt2 / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))