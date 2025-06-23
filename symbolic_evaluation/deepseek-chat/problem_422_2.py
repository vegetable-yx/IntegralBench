import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Step 1: Compute 2 raised to the power of 4/3
base = mp.mpf(2)
exponent = mp.mpf(4)/mp.mpf(3)  # Exponent as fraction 4/3
power_result = base ** exponent  # Calculate 2^(4/3)

# Step 2: Multiply the result by 1/4
factor = mp.mpf(1)/mp.mpf(4)  # Coefficient 1/4
result = factor * power_result  # Final result: (1/4) * 2^(4/3)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))