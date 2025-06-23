import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 7! using gamma function (gamma(n) = (n-1)!)
result = mp.gamma(8)  # 8! = 40320? Wait wait, wait. Wait 7! is 5040. So gamma(8) is 7! because gamma(n) = (n-1)!. So 8-1=7. So yes, gamma(8) is 7! = 5040. So the code is correct.

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))