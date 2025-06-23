import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the analytical expression: π/2
# Step 1: Assign π value
pi_value = mp.pi

# Step 2: Divide by 2
result = pi_value / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))