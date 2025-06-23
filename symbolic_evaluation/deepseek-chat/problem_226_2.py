import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Step 1: Get the value of pi
pi_val = mp.pi

# Step 2: Square pi to get pi squared
pi_squared = mp.power(pi_val, 2)

# Step 3: Divide by 4 to get the result
result = pi_squared / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))