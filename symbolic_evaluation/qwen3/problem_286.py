import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute components step by step
sqrt2 = mp.sqrt(2)  # Calculate square root of 2
ln_term = mp.log(1 + sqrt2)  # Compute natural logarithm term

# Calculate first part of the expression: (π/8) * ln^2(1+√2)
squared_log = ln_term ** 2
pi_over_8 = mp.pi / 8
first_term = pi_over_8 * squared_log

# Calculate second part of the expression: (1/4) * ln(1+√2)
second_term = (1/4) * ln_term  # Using integer division 1/4 would be 0, but in Python 3 it's 0.25

# Combine terms for final result
result = first_term - second_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))