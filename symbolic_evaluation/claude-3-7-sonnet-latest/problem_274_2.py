import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute sinh(5) using mpmath hyperbolic sine
sinh_value = mp.sinh(5)

# Subtract 1 from the computed sinh value
diff = sinh_value - 1

# Multiply by the constant factor 125/2
result = (mp.mpf(125) / mp.mpf(2)) * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))