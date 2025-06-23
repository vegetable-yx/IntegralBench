import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the Euler-Mascheroni constant
euler_gamma = mp.euler

# Compute the expression: 1 - γ
result = 1 - euler_gamma

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))