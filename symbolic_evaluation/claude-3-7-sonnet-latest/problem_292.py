import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Step 1: Compute Gamma(1/4)
gamma_val = mp.gamma(0.25)

# Step 2: Raise Gamma(1/4) to the 4th power
gamma_power4 = gamma_val**4

# Step 3: Multiply by pi
numerator = mp.pi * gamma_power4

# Step 4: Divide by 64 to get the final result
result = numerator / 64

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))