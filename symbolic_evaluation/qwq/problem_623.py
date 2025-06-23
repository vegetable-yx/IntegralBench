import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate arcsin(1/3) using mpmath's asin function
arcsin_value = mp.asin(1/3)

# Multiply the result by π
result = mp.pi * arcsin_value

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))