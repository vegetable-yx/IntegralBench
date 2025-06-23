import mpmath as mp
mp.dps = 15

# Calculate pi^4 using mpmath's constant
pi_squared = mp.pi ** 2
pi_power4 = pi_squared ** 2

# Compute the final result by dividing by 120
result = pi_power4 / 120

print(mp.nstr(result, n=10))