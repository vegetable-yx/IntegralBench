import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the first term: (π/4) * arctan(1/√2)
# Step 1: Calculate 1/sqrt(2)
inv_sqrt2 = 1 / mp.sqrt(2)

# Step 2: Compute arctan(1/sqrt(2))
atan_term = mp.atan(inv_sqrt2)

# Step 3: Multiply by π/4
first_term = (mp.pi / 4) * atan_term

# Compute the second term: (1/4) * ln(2)
# Step 1: Compute natural logarithm of 2
ln2 = mp.log(2)

# Step 2: Multiply by 1/4
second_term = (1/4) * ln2

# Combine the terms: first_term minus second_term
result = first_term - second_term

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))