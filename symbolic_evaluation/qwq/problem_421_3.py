import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate sin(1) using mpmath's sin function
angle = mp.mpf(1)
result = mp.sin(angle)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))