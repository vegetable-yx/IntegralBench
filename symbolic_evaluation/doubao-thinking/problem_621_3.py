import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Step 1: Access the constant pi
pi_value = mp.pi

# Step 2: Divide pi by 2
half_pi = pi_value / 2

# Step 3: Apply the negative sign to get the final result
result = -half_pi

# Output the result rounded to 10 decimal places
print(mp.nstr(result, n=10))