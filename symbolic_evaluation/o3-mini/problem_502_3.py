import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Step 1: Compute the natural logarithm of 2
ln2 = mp.log(2)

# Step 2: Multiply the logarithm by 60
term = 60 * ln2

# Step 3: Add the constant 10747 to the term
numerator = 10747 + term

# Step 4: Divide the numerator by 10 to get the final result
result = numerator / 10

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))