import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi squared by breaking into intermediate steps
# Step 1: Assign the constant pi
pi_value = mp.pi

# Step 2: Compute the square of pi
result = pi_value * pi_value

# Output the result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))