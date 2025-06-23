import mpmath as mp

# Set the internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the sine integral of 1
si_value = mp.si(1)

# Multiply the result by 4 as per the analytical expression
result = 4 * si_value

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))