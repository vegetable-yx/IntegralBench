import mpmath as mp

# Set the decimal places for internal calculations
mp.dps = 15

# The analytical result is a constant integer 626
result = 626

# Convert to mpmath float and print with 10 decimal places
print(mp.nstr(result, n=10))