import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the analytical expression: -2023/2022
# Step 1: Convert numerator and denominator to mpmath floats
numerator = mp.mpf(2023)
denominator = mp.mpf(2022)

# Step 2: Compute the fraction
fraction = numerator / denominator

# Step 3: Apply the negative sign
result = -fraction

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))