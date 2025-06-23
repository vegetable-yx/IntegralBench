import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute natural logarithm of 2
ln2 = mp.log(2)

# Step 2: Raise ln2 to the 4th power
ln2_4 = ln2 ** 4

# Step 3: Divide by 4 to get the final result
result = ln2_4 / 4

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))