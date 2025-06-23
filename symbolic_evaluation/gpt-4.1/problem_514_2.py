import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/6
pi_over_six = mp.pi / 6

# Calculate √3
sqrt_three = mp.sqrt(3)

# Calculate (√3)/8
sqrt_three_over_eight = sqrt_three / 8

# Sum the two components
result = pi_over_six + sqrt_three_over_eight

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))