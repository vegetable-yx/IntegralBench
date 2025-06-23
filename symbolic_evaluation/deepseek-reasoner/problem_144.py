import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate e^2 using mpmath's exponential function
e_squared = mp.exp(2)

# Calculate e^-2 using mpmath's exponential function
e_neg2 = mp.exp(-2)

# Compute the numerator: e^2 + 3*e^-2
numerator = e_squared + 3 * e_neg2

# Final result by dividing numerator by 8
result = numerator / 8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))