import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Step 1: Compute e^2 using mp.exp
e_squared = mp.exp(2)

# Step 2: Add 1 to the result of e^2
numerator = e_squared + 1

# Step 3: Multiply the numerator by 1/4 to get the final result
result = numerator / 4

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))