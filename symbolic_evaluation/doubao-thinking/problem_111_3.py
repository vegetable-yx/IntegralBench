import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_squared = mp.power(mp.pi, 2)

# Subtract 8 from pi squared
diff = pi_squared - 8

# Multiply by the square root of 2
result = mp.sqrt(2) * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))