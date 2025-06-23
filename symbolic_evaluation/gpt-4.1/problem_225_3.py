import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Step-by-step calculation of π³/8
# Compute π (using mpmath's built-in constant)
pi_val = mp.pi

# Cube π
pi_cubed = pi_val ** 3

# Divide by 8
result = pi_cubed / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))