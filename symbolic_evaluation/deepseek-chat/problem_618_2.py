import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Retrieve the Euler-Mascheroni constant γ
gamma = mp.euler

# Compute the expression: 1 - γ
result = 1 - gamma

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))