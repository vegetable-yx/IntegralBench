import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute the exact result from analytical solution
result = mp.mpf(9)  # Convert integer to mpmath floating-point number

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))