import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Step 1: Get the constant pi
pi_val = mp.pi

# Step 2: Square pi
pi_squared = pi_val ** 2

# Step 3: Divide by 16
result = pi_squared / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))