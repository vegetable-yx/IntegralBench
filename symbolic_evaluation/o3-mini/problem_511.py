import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Step 1: Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Step 2: Multiply by 2 to get 2*sqrt(2)
two_sqrt2 = 2 * sqrt2

# Step 3: Compute the sine of (2*sqrt(2))
sin_val = mp.sin(two_sqrt2)

# Step 4: Multiply the sine result by 2 to get final value
result = 2 * sin_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))