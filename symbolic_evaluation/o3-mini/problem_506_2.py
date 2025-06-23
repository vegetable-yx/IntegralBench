import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical answer is a constant: 1005
# Assign the constant value to 'result'
result = mp.mpf('1005')

# Print the result with 10 significant digits, ensuring trailing zeros are shown
print(mp.nstr(result, n=10, strip_zeros=False))