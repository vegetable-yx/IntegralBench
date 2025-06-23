import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 2 using mpmath
sqrt_2 = mp.sqrt(2)

# Compute the denominator 2*sqrt(2)
denominator = 2 * sqrt_2

# Calculate the final result by dividing pi by the denominator
result = mp.pi / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))