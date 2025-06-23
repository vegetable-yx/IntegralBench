import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the Euler-Mascheroni constant
gamma = mp.euler

# Compute the expression: 1 - γ
result = 1 - gamma

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))