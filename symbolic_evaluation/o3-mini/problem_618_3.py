import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Euler-Mascheroni constant γ
gamma_constant = mp.euler

# Calculate the result: 1 - γ
result = 1 - gamma_constant

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))