import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sine and cosine of 2
sin_2 = mp.sin(2)
cos_2 = mp.cos(2)

# Calculate the sine integral of 2
si_2 = mp.si(2)

# Combine all components according to the formula
sum_terms = sin_2 + cos_2 - 1 + si_2

# Multiply by 1/2 to get the final result
result = sum_terms * 0.5

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))