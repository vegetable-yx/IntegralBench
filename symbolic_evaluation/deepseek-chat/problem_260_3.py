import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Struve function H_0(1)
struve_val = mp.struveh(0, 1)

# Multiply by pi/4 to get the result
result = (mp.pi / 4) * struve_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))