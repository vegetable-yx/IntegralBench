import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the sine integral of 2
si_2 = mp.si(2)

# Calculate sin(2)
sin_2 = mp.sin(2)

# Compute the difference between sine integral and sine values
numerator = si_2 - sin_2

# Divide the result by 4 to get final value
result = numerator / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))