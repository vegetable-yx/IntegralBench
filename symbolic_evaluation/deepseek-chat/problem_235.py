import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the first term: 2/3
term1 = mp.mpf(2) / mp.mpf(3)

# Calculate the second term: (8 * sqrt(3) * pi) / 27
# Step 1: Compute square root of 3
sqrt3 = mp.sqrt(3)
# Step 2: Multiply by 8 and pi
numerator = mp.mpf(8) * sqrt3 * mp.pi
# Step 3: Divide by 27
term2 = numerator / mp.mpf(27)

# Sum the two terms to get the final result
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))