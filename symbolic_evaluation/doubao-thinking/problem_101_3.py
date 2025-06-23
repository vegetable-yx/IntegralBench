import mpmath as mp
mp.dps = 15

# Calculate complete elliptic integral of the second kind at 1/4
E_val = mp.ellipe(mp.mpf('0.25'))

# Multiply by 1/8 to get final result
result = E_val * mp.mpf('0.125')

print(mp.nstr(result, n=10))