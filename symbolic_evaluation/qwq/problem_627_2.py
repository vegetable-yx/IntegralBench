import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/4 component
pi_term = mp.pi / 4

# Calculate (ln 2)/2 component
ln2_term = mp.log(2) / 2

# Combine all components: π/4 + ln(2)/2 - 1
result = pi_term + ln2_term - 1

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))