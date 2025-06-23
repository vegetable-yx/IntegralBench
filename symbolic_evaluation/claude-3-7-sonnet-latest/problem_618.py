import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Euler-Mascheroni constant (γ) using mpmath's built-in constant
result = mp.euler

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))