import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute the two terms of the expression
term1 = (2 * mp.pi) / 3  # Calculate 2π/3
term2 = 4 * mp.sqrt(3)   # Calculate 4√3

# Sum the terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))