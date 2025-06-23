import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Euler-Mascheroni constant (gamma)
gamma = mp.euler

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute the expression: -gamma - 2*ln(2)
result = -gamma - 2*ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))