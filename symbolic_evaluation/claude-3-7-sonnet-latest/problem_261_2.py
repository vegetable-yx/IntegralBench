import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sin(2) radians
sin_val = mp.sin(2)

# Divide by 4 and apply negative sign
result = -sin_val / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))