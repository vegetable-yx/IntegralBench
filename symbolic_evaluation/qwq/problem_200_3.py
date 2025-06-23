import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate the sine integral of 1 using mpmath's built-in function
si_value = mp.si(1)

# Multiply by 4 according to the analytical expression
result = 4 * si_value

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))