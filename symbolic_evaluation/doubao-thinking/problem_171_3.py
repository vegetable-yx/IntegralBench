import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the constants and parameters
a = mp.mpf('0.5')
b = mp.mpf('0.25')
c = mp.mpf('0.125')

# Compute intermediate terms
term1 = (mp.pi * a**4 * mp.log(a) / 32) * (mp.ellipk(a) - mp.ellipe(a))
term2 = (mp.pi * a**2 / 64) * (mp.ellipk(a) - mp.ellipe(a))
term3 = (mp.pi / 128) * (mp.ellipk(a) - mp.ellipe(a))
term4 = (mp.pi * a**4 / 64) * (mp.ellipe(a) - (1 - a**2) * mp.ellipk(a))

# Combine the terms to get the result
result = term1 - term2 - term3 + term4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))