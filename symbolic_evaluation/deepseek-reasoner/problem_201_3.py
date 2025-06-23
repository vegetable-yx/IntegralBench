import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sin(1) using mpmath's sine function
sin_1 = mp.sin(1)

# Calculate cos(1) using mpmath's cosine function
cos_1 = mp.cos(1)

# Sum the trigonometric function results
sum_trig = sin_1 + cos_1

# Subtract 1 from the trigonometric sum
adjusted_sum = sum_trig - 1

# Multiply by 2 to get the final result
result = 2 * adjusted_sum

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))