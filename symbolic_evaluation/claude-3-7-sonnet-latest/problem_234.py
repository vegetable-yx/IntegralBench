import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Step 2: Multiply sqrt(2) by 2
two_sqrt2 = 2 * sqrt2

# Step 3: Subtract the result from 8
numerator_part = 8 - two_sqrt2

# Step 4: Multiply by pi
pi_times_numerator = mp.pi * numerator_part

# Step 5: Divide by 3 to get the final result
result = pi_times_numerator / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))