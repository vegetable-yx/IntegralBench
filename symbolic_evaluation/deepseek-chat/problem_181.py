import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the sine integral of 2
si_val = mp.si(2)

# Calculate the sine of 2 radians
sin_val = mp.sin(2)

# Compute the difference: Si(2) - sin(2)
diff = si_val - sin_val

# Multiply by 2/π to get the final result
result = (2 / mp.pi) * diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))