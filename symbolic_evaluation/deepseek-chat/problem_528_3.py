import mpmath as mp

# Set the internal decimal precision to 15 for sufficient accuracy
mp.dps = 15

# Step 1: Compute e (the base of the natural logarithm)
e_const = mp.e

# Step 2: Compute (e - 1)
e_minus_one = e_const - 1

# Step 3: Compute exp(e - 1)
exp_e_minus_one = mp.exp(e_minus_one)

# Step 4: Compute the final result: exp(e - 1) - e
result = exp_e_minus_one - e_const

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))