import mpmath as mp
mp.dps = 15  # Set decimal precision to 15 for intermediate calculations

# Calculate components of the expression step by step
sqrt5 = mp.sqrt(5)  # Compute square root of 5
golden_ratio = (1 + sqrt5) / 2  # Calculate (1 + √5)/2 (golden ratio)
log_term = mp.log(golden_ratio)  # Compute natural logarithm of golden ratio
pi_half = mp.pi / 2  # Precompute π/2

# Multiply components to get final result
result = pi_half * log_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))