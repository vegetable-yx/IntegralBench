import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# The analytical expression is the Euler-Mascheroni constant (γ)
# This is a fundamental constant in mpmath, accessible via mp.euler
result = mp.euler

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))