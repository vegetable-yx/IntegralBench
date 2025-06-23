import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate components of the expression
pi_over_2 = mp.pi / 2  # Calculate π/2
sqrt_pi_over_2 = mp.sqrt(pi_over_2)  # Square root of π/2

sin_1 = mp.sin(1)  # Calculate sin(1)
cos_1 = mp.cos(1)  # Calculate cos(1)

sum_trig = sin_1 + cos_1  # Sum of trigonometric terms

# Combine all components for final result
result = sqrt_pi_over_2 * sum_trig

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))