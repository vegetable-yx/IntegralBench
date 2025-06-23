import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Step 1: Compute the natural logarithm of 3
ln3 = mp.log(3)

# Step 2: Compute π (pi) divided by 4
pi_over_4 = mp.pi / 4

# Step 3: Multiply the two results to get the final value
result = pi_over_4 * ln3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))