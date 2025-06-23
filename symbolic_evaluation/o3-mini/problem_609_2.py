import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Step 1: Compute the value of pi
pi_value = mp.pi

# Step 2: Divide pi by 2 to get pi/2
half_pi = pi_value / 2

# Step 3: Subtract pi/2 from 1 to obtain the final result
result = 1 - half_pi

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))