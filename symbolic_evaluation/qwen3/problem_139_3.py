import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e^2 using mpmath
e_squared = mp.exp(2)

# Calculate e^-2 using mpmath
e_neg2 = mp.exp(-2)

# Combine terms according to the expression e^2 + e^-2 - 2
result = e_squared + e_neg2 - 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))