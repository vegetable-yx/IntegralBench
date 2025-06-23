import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt_val = mp.sqrt(2)

# Step 2: Multiply the square root by 2
inner_product = 2 * sqrt_val

# Step 3: Compute the sine of the inner product
sin_val = mp.sin(inner_product)

# Step 4: Multiply the sine result by 2
result = 2 * sin_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))