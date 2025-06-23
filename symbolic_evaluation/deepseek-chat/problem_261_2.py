import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Struve H function of order 0 at 2
struve_val = mp.struveh(0, 2)

# Multiply by pi/4
term = (mp.pi / 4) * struve_val

# Subtract 1/2 to get the final result
result = term - 0.5

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))