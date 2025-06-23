import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute zeta(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Multiply zeta(3) by 7
seven_zeta = 7 * zeta3

# Divide the result by 2 to get the final value
result = seven_zeta / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))