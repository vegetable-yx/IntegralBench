import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π squared
pi_sq = mp.pi**2

# Calculate 4 * π * ln(2)
four_pi_ln2 = 4 * mp.pi * mp.log(2)

# Sum π squared and 4π ln(2)
sum_pi_terms = pi_sq + four_pi_ln2

# Calculate (√2 - 1)
sqrt2_minus_1 = mp.sqrt(2) - 1

# Multiply the two parts to get the numerator
numerator = sum_pi_terms * sqrt2_minus_1

# Divide by 32 to get the final result
result = numerator / 32

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))