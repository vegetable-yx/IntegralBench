import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant denominator
denom = mp.mpf(2023)

# Initialize the sum to zero
total_sum = mp.mpf(0)

# Sum over m from -2022 to 2022 (inclusive)
for m in range(-2022, 2023):
    # Compute the argument: m/2023
    arg = m / denom
    # Compute arcsin using mp.asin and accumulate
    total_sum += mp.asin(arg)

# Calculate the main expression: 4045*pi - 2*sum
result = 4045 * mp.pi - 2 * total_sum

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))