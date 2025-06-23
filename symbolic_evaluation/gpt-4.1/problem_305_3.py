import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Step 1: Compute the square root of 5
sqrt5 = mp.sqrt(5)

# Step 2: Compute the fraction (1 + sqrt(5)) / 2
fraction = (1 + sqrt5) / 2

# Step 3: Take the natural logarithm of the fraction
log_val = mp.log(fraction)

# Step 4: Multiply by 1/4 to get the final result
result = (1/4) * log_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))