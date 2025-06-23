import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt3 = mp.sqrt(3)  # Compute square root of 3
e3 = mp.exp(3)      # Compute e^3
e_neg3 = mp.exp(-3) # Compute e^(-3)

# Calculate terms in the numerator
term1 = e3 * (3 + 2*sqrt3)
term2 = e_neg3 * (3 - 2*sqrt3)

# Combine terms and divide by 4
total = term1 + term2
result = total / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))