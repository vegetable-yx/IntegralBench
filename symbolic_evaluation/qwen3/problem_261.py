import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the sine integral of 2
si_value = mp.si(2)

# Multiply by 1/2 to get the final result
result = 0.5 * si_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))