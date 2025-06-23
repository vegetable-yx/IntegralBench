import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Step 1: Compute ln(2)
ln2 = mp.log(2)

# Step 2: Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Step 3: Compute the argument for the second logarithm: (1 + sqrt(2)) / 2
log_arg = (1 + sqrt2) / 2

# Step 4: Compute ln( (1+sqrt(2))/2 )
ln_term = mp.log(log_arg)

# Step 5: Compute the first term: -2 * pi * ln(2)
term1 = -2 * mp.pi * ln2

# Step 6: Compute the second term: 4 * pi * ln( (1+sqrt(2))/2 )
term2 = 4 * mp.pi * ln_term

# Step 7: Sum the two terms
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))