import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute pi using mpmath constant
pi_val = mp.pi

# Step 2: Compute square root of 5
sqrt5 = mp.sqrt(5)

# Step 3: Compute (pi * sqrt(5)) / 2
fraction = (pi_val * sqrt5) / 2

# Step 4: Subtract fraction from pi
result = pi_val - fraction

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))