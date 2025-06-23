import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Euler-Mascheroni constant (γ)
gamma = mp.euler

# Compute the expression: 1 - γ
result = 1 - gamma

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))