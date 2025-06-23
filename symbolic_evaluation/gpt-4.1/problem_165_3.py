import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Step 1: Get the constant pi
pi_val = mp.pi

# Step 2: Calculate tanh(pi)
tanh_pi = mp.tanh(pi_val)

# Step 3: Compute (pi * tanh(pi)) / 2
numerator = pi_val * tanh_pi
result = numerator / 2

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))