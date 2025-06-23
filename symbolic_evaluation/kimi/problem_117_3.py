import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Step 1: Calculate pi to the fourth power
pi_squared = mp.pi ** 2
pi_fourth = pi_squared ** 2

# Step 2: Divide the result by 16
result = pi_fourth / 16

# Output the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))