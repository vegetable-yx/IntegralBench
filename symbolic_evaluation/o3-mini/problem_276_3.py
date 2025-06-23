import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# USER MUST SET VALUES FOR a AND b BELOW
a = 1.0  # Replace with desired value for a
b = 1.0  # Replace with desired value for b

# Calculate square root of a
sqrt_a = mp.sqrt(a)

# Compute argument for hypergeometric function: (a^2 * b^2)/4
arg = (a**2 * b**2) / 4

# Evaluate confluent hypergeometric function 0F1(; 3/2; arg)
hyp_val = mp.hyp0f1(1.5, arg)  # 3/2 = 1.5

# Compute final result: 2 * sqrt(a) * hypergeometric_value
result = 2 * sqrt_a * hyp_val

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))