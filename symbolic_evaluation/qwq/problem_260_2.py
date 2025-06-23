import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the Sine Integral of 1
si_1 = mp.si(1)

# Compute sin(1)
sin_1 = mp.sin(1)

# Calculate π/2 * sin(1)
pi_over_2_times_sin1 = (mp.pi / 2) * sin_1

# Combine all terms according to the formula
result = si_1 + pi_over_2_times_sin1 - sin_1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))