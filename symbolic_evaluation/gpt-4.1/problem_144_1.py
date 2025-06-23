import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute sinh(1) using mpmath function
sinh_value = mp.sinh(1)

# Square the hyperbolic sine value
sinh_squared = sinh_value ** 2

# Calculate the final result by dividing by 12
result = sinh_squared / 12

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))