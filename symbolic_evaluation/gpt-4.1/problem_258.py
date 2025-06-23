import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute e^{-0.25}
exponential_term = mp.exp(-0.25)

# Step 2: Compute square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Step 3: Multiply exponential term by sqrt(pi)
product = exponential_term * sqrt_pi

# Step 4: Multiply by the constant factor 2
result = 2 * product

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))