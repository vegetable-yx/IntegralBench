import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute sine integral Si(4)
si_val = mp.si(4)

# Multiply Si(4) by 4
part1 = 4 * si_val

# Compute sin(2) and multiply by 4
part2 = 4 * mp.sin(2)

# Compute cos(2), multiply by -pi
part3 = -mp.pi * mp.cos(2)

# Constant term: -pi
part4 = -mp.pi

# Sum all parts
total = part1 + part2 + part3 + part4

# Divide by 8*pi
result = total / (8 * mp.pi)

# Print result to 10 decimal places
print(mp.nstr(result, n=10))