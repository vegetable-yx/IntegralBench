import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Step 1: Compute the natural logarithm of 2
ln2 = mp.log(2)

# Step 2: Calculate the reciprocal of ln(2)
reciprocal_ln2 = 1 / ln2

# Step 3: Add 2 to the reciprocal
result = reciprocal_ln2 + 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))