import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi^4 divided by 1024 using exact mathematical operations
pi_val = mp.pi  # Get mpmath's high-precision π constant
pi_squared = pi_val ** 2  # Calculate π²
pi_power4 = pi_squared ** 2  # Square π² to get π⁴
result = pi_power4 / 1024  # Divide by 1024 for final result

print(mp.nstr(result, n=10))  # Print result with exactly 10 decimal places