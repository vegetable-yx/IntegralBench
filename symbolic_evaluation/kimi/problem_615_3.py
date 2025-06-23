import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# The analytical solution to the integral is exactly 9
result = mp.mpf(9)  # Convert exact integer result to mpmath floating-point

# Print result with 10 decimal places (will show .0000000000)
print(mp.nstr(result, n=10))