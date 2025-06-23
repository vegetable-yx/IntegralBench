import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the sum of 1/n² from n=2 to infinity using known zeta(2) value
sum_n_squared = mp.pi**2 / 6 - 1

# Apply the negative sign from the original expression
result = -sum_n_squared

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))