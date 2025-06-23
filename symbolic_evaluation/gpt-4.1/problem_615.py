import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute sqrt(50)
sqrt50 = mp.sqrt(50)

# Step 2: Compute the two terms inside the cube roots
inner_plus = sqrt50 + 7
inner_minus = sqrt50 - 7

# Step 3: Compute cube roots using exponentiation
A = mp.power(inner_plus, mp.mpf(1)/3)  # cube root of (sqrt(50) + 7)
B = mp.power(inner_minus, mp.mpf(1)/3)  # cube root of (sqrt(50) - 7)

# Step 4: Compute C = A - B
C = A - B

# Step 5: Compute powers of C
C_squared = C**2
C_fourth = C**4

# Step 6: Compute the two terms of the expression
term1 = (mp.mpf(3)/8) * C_fourth
term2 = (mp.mpf(3)/4) * C_squared

# Step 7: Sum the terms for final result
result = term1 + term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))