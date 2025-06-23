import mpmath as mp

# Set internal decimal precision to 15 digits for calculations
mp.dps = 15

# Calculate the exact value: -7π/8
# Step 1: Compute π (using mpmath's built-in constant)
pi_val = mp.pi

# Step 2: Multiply π by 7
numerator = 7 * pi_val

# Step 3: Divide by 8
fraction = numerator / 8

# Step 4: Apply the negative sign
result = -fraction

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))