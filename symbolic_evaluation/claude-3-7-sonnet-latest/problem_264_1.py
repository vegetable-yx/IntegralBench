import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute sin(2) where 2 is in radians
sin_val = mp.sin(2)

# Add the value of pi to sin(2)
numerator = mp.pi + sin_val

# Divide the sum by 4
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))