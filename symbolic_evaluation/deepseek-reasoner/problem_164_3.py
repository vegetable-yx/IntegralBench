import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π^4
pi_power4 = mp.power(mp.pi, 4)

# Calculate (15/2) * π^4
term = mp.fmul(15/2, pi_power4)

# Add 384 constant term
result = mp.fadd(384, term)

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))