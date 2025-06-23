import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute π using mpmath constant
pi_val = mp.pi

# Step 2: Calculate π cubed
pi_cubed = pi_val ** 3

# Step 3: Divide π cubed by 24 to get the final result
result = pi_cubed / 24

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))