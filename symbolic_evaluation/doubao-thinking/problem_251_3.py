import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression step by step
sqrt5 = mp.sqrt(5)  # Compute square root of 5
golden_ratio = (1 + sqrt5) / 2  # Calculate (1 + √5)/2
log_term = mp.log(golden_ratio)  # Compute natural logarithm of the golden ratio

# Multiply by 2π to get final result
result = 2 * mp.pi * log_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))