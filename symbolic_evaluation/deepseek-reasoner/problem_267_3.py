import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the trilogarithm term Li_3(1/4)
li3_term = mp.polylog(3, 1/4)

# Multiply by π and divide by 8
result = (mp.pi / 8) * li3_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))