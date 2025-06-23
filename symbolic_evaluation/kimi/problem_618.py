import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Retrieve the Euler-Mascheroni constant γ
gamma_constant = mp.euler

# Compute the expression: 1 - γ
result = 1 - gamma_constant

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))