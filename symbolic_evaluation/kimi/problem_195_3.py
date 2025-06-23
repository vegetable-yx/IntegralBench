import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide pi squared by 8 to get the first term
term1 = pi_squared / 8

# Calculate pi divided by 2 (second term)
term2 = mp.pi / 2

# Subtract the second term from the first term
intermediate_result = term1 - term2

# Add 1 to complete the expression: π²/8 - π/2 + 1
result = intermediate_result + 1

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))