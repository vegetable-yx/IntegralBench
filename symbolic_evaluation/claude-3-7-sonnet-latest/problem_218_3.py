import mpmath as mp

# Set internal decimal precision to 15 digits for intermediate calculations
mp.dps = 15

# Step 1: Compute π (pi) using mpmath constant
pi_val = mp.pi

# Step 2: Compute π cubed
pi_cubed = pi_val ** 3

# Step 3: Divide π cubed by 108
result = pi_cubed / 108

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))