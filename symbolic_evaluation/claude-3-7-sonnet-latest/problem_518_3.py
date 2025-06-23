import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is the constant 4036
result = mp.mpf(4036)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10, strip_zeros=False))

The code sets the internal precision to 15 decimal places using `mp.dps = 15`. The constant value 4036 is converted to an mpmath floating-point number using `mp.mpf(4036)`. The result is printed with `mp.nstr` using `n=10` to specify 10 decimal places and `strip_zeros=False` to ensure trailing zeros are displayed, meeting the requirement of exactly 10 decimal places. The output will be `4036.0000000000`.