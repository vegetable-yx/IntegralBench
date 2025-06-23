import mpmath as mp

# Set internal decimal precision to 15 for sufficient accuracy
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt_two = mp.sqrt(2)

# Step 2: Subtract 1 from sqrt(2)
diff = sqrt_two - 1

# Step 3: Multiply by pi
result = mp.pi * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))