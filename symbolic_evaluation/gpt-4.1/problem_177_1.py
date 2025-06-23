import mpmath as mp
mp.dps = 15

# Calculate the sine integral of 3
si_3 = mp.si(3)

# Multiply by π to get the final result
result = mp.pi * si_3

# Output the result with 10 decimal precision
print(mp.nstr(result, n=10))