import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Euler-Mascheroni constant γ
euler_gamma = mp.euler

# Compute 1 - γ
result = 1 - euler_gamma

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))