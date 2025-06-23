import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Define the analytical expression for the integral
# Intermediate calculations for each term
term1 = mp.pi**2 / 128
term2 = -3 * mp.pi * mp.sqrt(3) / 256
term3 = mp.pi * mp.log(2) / 128
term4 = -mp.log(3) / 256

# Combine all terms to get the final result
result = term1 + term2 + term3 + term4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))