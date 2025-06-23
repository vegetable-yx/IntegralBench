import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Step 1: Access the constant pi from mpmath
pi_value = mp.pi

# Step 2: Divide pi by 4 to obtain the result
result = pi_value / 4

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))