import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15
# Disable pretty printing to ensure trailing zeros are shown
mp.pretty = False

# The analytical expression is a constant: 99
# Convert the constant to an mpmath floating-point number
result = mp.mpf(99)

# Print the result with exactly 10 significant digits
print(mp.nstr(result, n=10))