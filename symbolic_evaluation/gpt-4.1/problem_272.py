import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the closed-form expression:
# result = (pi/2) * [ (sqrt(2) - 1) - ln((1 + sqrt(2))/2) ]

# Step 1: Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Step 2: Compute term1 = sqrt(2) - 1
term1 = sqrt2 - 1

# Step 3: Compute term2 = (1 + sqrt(2)) / 2
term2 = (1 + sqrt2) / 2

# Step 4: Compute term3 = ln(term2) = ln((1 + sqrt(2))/2)
term3 = mp.log(term2)

# Step 5: Compute factor = term1 - term3
factor = term1 - term3

# Step 6: Compute result = (pi/2) * factor
result = (mp.pi / 2) * factor

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))