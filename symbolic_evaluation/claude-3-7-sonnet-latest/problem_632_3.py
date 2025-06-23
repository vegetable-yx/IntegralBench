import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Step 1: Compute the natural logarithm of 2 using mp.log
ln2 = mp.log(2)

# Step 2: Apply the negative sign to obtain the final result
result = -ln2

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))