import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Retrieve Euler-Mascheroni constant
gamma_constant = mp.euler

# Compute negative of the constant
result = -gamma_constant

# Print result to 10 decimal places
print(mp.nstr(result, n=10))