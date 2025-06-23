import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the closed-form expression: (11 * pi^3)/216 + ln(2) * Catalan's constant
term1 = (11 * mp.pi**3) / 216
term2 = mp.log(2) * mp.catalan
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))