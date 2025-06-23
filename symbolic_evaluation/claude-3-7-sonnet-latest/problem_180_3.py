import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant factor: 2^(5/4)
two_power = mp.power(2, mp.mpf(5)/4)

# Compute the denominator: sqrt(2 * pi)
denominator = mp.sqrt(2 * mp.pi)

# Compute the trigonometric argument: sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute the trigonometric part: sin(sqrt(2)) - cos(sqrt(2))
trig_part = mp.sin(sqrt2) - mp.cos(sqrt2)

# Combine all parts: (2^(5/4) / sqrt(2*pi) * (sin(sqrt(2)) - cos(sqrt(2)))
result = (two_power / denominator) * trig_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))