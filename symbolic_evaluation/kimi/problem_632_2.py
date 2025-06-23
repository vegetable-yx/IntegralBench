import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the sum of 1/n² from n=2 to infinity using Riemann zeta function
sum_series = mp.zeta(2) - 1  # Subtract n=1 term (1/1²)

# Apply the negative sign from the original expression
result = -sum_series

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))