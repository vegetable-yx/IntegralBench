import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the denominator = 2*sqrt(2)
denominator = 2 * mp.sqrt(2)

# Compute the final result as pi divided by the calculated denominator
result = mp.pi / denominator

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))