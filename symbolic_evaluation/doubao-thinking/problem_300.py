import mpmath as mp
mp.dps = 15  # Set internal precision

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Calculate 4 times ln(2)
four_ln2 = 4 * ln2

# Subtract 1 from the previous result
subtracted_value = four_ln2 - 1

# Multiply by pi to get the numerator
numerator = mp.pi * subtracted_value

# Divide by 32 to obtain the final result
result = numerator / 32

print(mp.nstr(result, n=10))