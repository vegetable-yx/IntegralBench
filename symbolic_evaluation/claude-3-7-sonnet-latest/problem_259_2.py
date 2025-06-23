import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Step 1: Compute the cosine of 1 radian
cos1 = mp.cos(1)

# Step 2: Calculate 1 - cos(1)
one_minus_cos1 = 1 - cos1

# Step 3: Multiply by pi to get the final result
result = mp.pi * one_minus_cos1

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))