import mpmath as mp

# Set internal decimal precision to 15 for reliable 10-digit output
mp.dps = 15

# Calculate π/6
pi_sixth = mp.pi / 6

# Calculate √3
sqrt_three = mp.sqrt(3)

# Calculate (√3)/8
sqrt_three_eighth = sqrt_three / 8

# Sum the two parts: π/6 + √3/8
result = pi_sixth + sqrt_three_eighth

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))