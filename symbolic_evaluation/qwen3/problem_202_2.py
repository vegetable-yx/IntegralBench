import mpmath as mp
mp.dps = 15

# Calculate sin(1) using mpmath
sin_1 = mp.sin(1)

# Calculate cos(1) using mpmath
cos_1 = mp.cos(1)

# Compute sum of trigonometric values
trig_sum = sin_1 + cos_1

# Subtract 1 from the trigonometric sum
adjusted_sum = trig_sum - 1

# Multiply by 2 to get final result
result = 2 * adjusted_sum

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))