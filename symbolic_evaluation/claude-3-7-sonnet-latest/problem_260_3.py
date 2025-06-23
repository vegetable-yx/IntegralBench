import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Calculate the sine integral Si(1)
si_one = mp.si(1)

# Compute the result: π/2 - Si(1)
result = pi_over_2 - si_one

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))