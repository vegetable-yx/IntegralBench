import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the constant pi/4
pi_over_4 = mp.pi / 4

# Compute the sine integral Si(3)
si_value = mp.si(3)

# Multiply to get the final result: (pi/4) * Si(3)
result = pi_over_4 * si_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))