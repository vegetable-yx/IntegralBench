import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate 2π/3 term
two_pi_over_3 = (2 * mp.pi) / 3

# Calculate 4√3 term
four_root_three = 4 * mp.sqrt(3)

# Sum the components
result = two_pi_over_3 + four_root_three

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))