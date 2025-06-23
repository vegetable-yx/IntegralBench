import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Catalan's constant (denoted as G in the expression)
G = mp.catalan

# Compute pi/8 multiplied by Catalan's constant
pi_val = mp.pi
result = (pi_val / 8) * G

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))