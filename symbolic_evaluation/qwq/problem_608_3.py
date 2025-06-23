import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Step 1: Compute the natural logarithm of 2
ln2 = mp.log(2)

# Step 2: Raise ln(2) to the fourth power
ln2_4 = ln2**4

# Step 3: Divide the result by 4
result = ln2_4 / 4

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))