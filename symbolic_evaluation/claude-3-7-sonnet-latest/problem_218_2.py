import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Compute the argument π/3
theta = mp.pi / 3

# Evaluate Clausen function of order 2 at π/3
cl2 = mp.clausen(2, theta)

# Evaluate Clausen function of order 3 at π/3
cl3 = mp.clausen(3, theta)

# Combine terms: ln(2) * Cl₂(π/3) + (1/2) * Cl₃(π/3)
result = ln2 * cl2 + 0.5 * cl3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))