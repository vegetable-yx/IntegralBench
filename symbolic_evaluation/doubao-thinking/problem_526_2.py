import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute natural logarithm of 3
ln3 = mp.log(3)

# Step 2: Multiply by pi
pi_ln3 = mp.pi * ln3

# Step 3: Divide by 4 to get the final result
result = pi_ln3 / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))