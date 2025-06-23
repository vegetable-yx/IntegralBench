import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute natural logarithm of 2
ln2 = mp.log(2)

# Step 2: Compute exponential of -6
exp_neg6 = mp.exp(-6)

# Step 3: Compute (1 - e^{-6})
one_minus_exp = 1 - exp_neg6

# Step 4: Multiply ln(2) by (1 - e^{-6})
product = ln2 * one_minus_exp

# Step 5: Divide the product by 6
result = product / 6

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))