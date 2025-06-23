import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute Euler-Mascheroni constant
gamma = mp.euler

# Calculate the expression: 1 - γ
result = 1 - gamma

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))