import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate components step by step
sqrt_2 = mp.sqrt(2)          # Compute sqrt(2)
log_argument = 1 + sqrt_2    # Compute 1 + sqrt(2)
log_term = mp.log(log_argument)  # Natural logarithm of (1+sqrt(2))
squared_log = log_term ** 2  # Square the logarithm term
result = (mp.pi / 8) * squared_log  # Multiply by pi/8

print(mp.nstr(result, n=10))