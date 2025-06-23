import mpmath as mp

# Set internal decimal precision to 15 for accurate intermediate calculations
mp.dps = 15

# Euler-Mascheroni constant
gamma_constant = mp.euler

# Compute the result: 1 - γ
result = 1 - gamma_constant

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))