import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Euler-Mascheroni constant (γ) is available as mp.euler
gamma_constant = mp.euler

# Compute the expression: 1 - γ
result = 1 - gamma_constant

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))