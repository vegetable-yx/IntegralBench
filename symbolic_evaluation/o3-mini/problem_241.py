import mpmath as mp

# Set internal decimal precision to 15 for reliable calculations
mp.dps = 15

# Step 1: Compute ln(2) using mp.log
ln2 = mp.log(2)

# Step 2: Multiply ln(2) by 2
two_ln2 = 2 * ln2

# Step 3: Subtract the result from 1
numerator = 1 - two_ln2

# Step 4: Divide by 4 to get final result
result = numerator / 4

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))