import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for trigonometric functions
trig_arg = 2 * mp.sqrt(2)

# Compute the trigonometric part: (sin(2√2)/(2√2) - cos(2√2)
trig_part = (mp.sin(trig_arg) / (2 * mp.sqrt(2))) - mp.cos(trig_arg)

# Compute Gamma(5/4) and square it
gamma_54 = mp.gamma(5/4)
gamma_sq = gamma_54**2

# Compute Gamma(5/2)
gamma_52 = mp.gamma(5/2)

# Compute the denominator: sqrt(2 * pi * sqrt(2))
denom = mp.sqrt(2 * mp.pi * mp.sqrt(2))

# Combine the constants: 8 * gamma_sq / (gamma_52 * denom)
const_factor = 8 * gamma_sq / (gamma_52 * denom)

# Multiply constant factor by trigonometric part
result = const_factor * trig_part

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))