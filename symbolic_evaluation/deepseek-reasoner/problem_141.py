import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate e^2
e_squared = mp.exp(2)

# Calculate e^-2
e_minus_two = mp.exp(-2)

# Compute numerator: 3e^2 - e^-2 - 2
numerator = 3 * e_squared - e_minus_two - 2

# Divide by 4 to get final result
result = numerator / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))