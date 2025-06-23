import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate sin(1)
sin_val = mp.sin(1)

# Calculate the sine integral Si(1)
si_val = mp.si(1)

# Compute the expression: 2 * (sin(1) - Si(1))
result = 2 * (sin_val - si_val)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))