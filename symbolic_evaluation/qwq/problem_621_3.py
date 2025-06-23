import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate the result using exact mathematical expression
pi_value = mp.pi  # Get mpmath's high-precision π
result = -pi_value / 2  # Compute -π/2

print(mp.nstr(result, n=10))  # Print result with 10 decimal places