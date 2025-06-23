import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Retrieve the Euler-Mascheroni constant (γ)
euler_mascheroni = mp.euler

# Compute 1 - γ
result = 1 - euler_mascheroni

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))