import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the sine integral of 2
si_value = mp.si(2)

# Multiply by 1/2 to get the final result
result = 0.5 * si_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))