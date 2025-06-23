import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define constants
n = 2023
j_low = -2021
j_high = 2022

# Initialize the sum to zero
total_sum = mp.mpf(0)

# Compute the denominator as an mpmath float
denom = mp.mpf(n)

# Calculate the sum: Σ arcsin(j/2023) from j=-2021 to 2022
for j in range(j_low, j_high + 1):
    arg = mp.mpf(j) / denom
    total_sum += mp.asin(arg)

# Compute the first term: 2022 * arcsin(2022/2023)
term1 = 2022 * mp.asin(mp.mpf(2022) / denom)

# Compute the constant term: 1011 * π
term3 = 1011 * mp.pi

# Combine terms: 2022*arcsin(...) - Σ + 1011*π
inner_expr = term1 - total_sum + term3

# Multiply by 2 for the final result
result = 2 * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))