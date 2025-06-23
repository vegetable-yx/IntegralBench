import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the sine integral of 2 using mpmath's built-in function
si_val = mp.si(2)

# Multiply by 1/2 to get the final result
result = 0.5 * si_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))