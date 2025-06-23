import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of parameter 'a' (user can modify this value)
a = 1.0  # Example value, can be changed as needed

# Compute the common argument for the hypergeometric functions
z = -a**2 / 4

# Calculate the first hypergeometric term: {}_1F_2(1/2; 3/4, 5/4; z)
term1 = mp.hyp1f2(0.5, 0.75, 1.25, z)

# Calculate the second hypergeometric term: {}_1F_2(3/2; 5/4, 7/4; z)
term2 = mp.hyp1f2(1.5, 1.25, 1.75, z)

# Compute the difference between the two hypergeometric terms
diff = term1 - term2

# Multiply by the prefactor (π*a/4)
result = (mp.pi * a / 4) * diff

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))