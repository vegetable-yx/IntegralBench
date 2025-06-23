import mpmath as mp

# Set the internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the first part (A): (729/6 + 243/5 + 81/4 + 27/3 + 9/2 + 3 + ln(2))
A = mp.mpf(729) / 6
A += mp.mpf(243) / 5
A += mp.mpf(81) / 4
A += mp.mpf(27) / 3
A += mp.mpf(9) / 2
A += mp.mpf(3)
A += mp.log(2)  # Natural logarithm of 2

# Compute the second part (B): (64/6 + 32/5 + 16/4 + 8/3 + 4/2 + 2)
B = mp.mpf(64) / 6
B += mp.mpf(32) / 5
B += mp.mpf(16) / 4
B += mp.mpf(8) / 3
B += mp.mpf(4) / 2
B += mp.mpf(2)

# Compute the difference: (A - B)
diff = A - B

# Multiply the difference by 6 to get the final result
result = 6 * diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))