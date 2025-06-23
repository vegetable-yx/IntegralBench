import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

pi_val = mp.pi  # Get the value from mpmath
pi_squared = pi_val ** 2  # Calculate π squared
result = pi_squared / 16  # Divide by 16 to get final value

print(mp.nstr(result, n=10))  # Print result with 10 decimal places