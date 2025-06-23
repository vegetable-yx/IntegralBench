import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the hyperbolic cosine of 2
cosh_2 = mp.cosh(2)

# Compute the final result by subtracting 1
result = cosh_2 - 1

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))