import mpmath as mp
mp.dps = 15

# Calculate the sine integral of 2
si_val = mp.si(2)

# Multiply by 1/2 to get final result
result = 0.5 * si_val

print(mp.nstr(result, n=10))