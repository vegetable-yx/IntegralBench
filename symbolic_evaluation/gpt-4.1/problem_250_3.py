import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt_two = mp.sqrt(2)

# Step 2: Subtract 1 from the square root of 2
sqrt_two_minus_one = sqrt_two - 1

# Step 3: Multiply by pi to get the final result
result = mp.pi * sqrt_two_minus_one

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))