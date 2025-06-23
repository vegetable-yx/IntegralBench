import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt_two = mp.sqrt(2)

# Step 2: Multiply by pi
pi_times_sqrt2 = mp.pi * sqrt_two

# Step 3: Divide the product by 2 to get the final result
result = pi_times_sqrt2 / 2

# Output the result with 10 decimal places
print(mp.nstr(result, n=10))