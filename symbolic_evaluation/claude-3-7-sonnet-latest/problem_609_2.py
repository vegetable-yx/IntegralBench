import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Calculate ln(2)
ln2 = mp.log(2)

# Step 2: Calculate -ln(2)
neg_ln2 = -ln2

# Step 3: Calculate 1/2
half = mp.mpf(1)/2

# Step 4: Combine the results: -ln(2) + 1/2
result = neg_ln2 + half

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))