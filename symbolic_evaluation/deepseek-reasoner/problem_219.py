import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate trigonometric components
sin1 = mp.sin(1)
cos1 = mp.cos(1)

# Combine trigonometric terms
trig_sum = sin1 + cos1
adjusted_sum = trig_sum - 1

# Compute final result
result = 2 * sqrt2 * adjusted_sum

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))