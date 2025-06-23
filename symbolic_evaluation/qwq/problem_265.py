import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate sin(2) using mpmath's sine function
sin_2 = mp.sin(2)

# Divide the result by 4 to get the final value
result = sin_2 / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))