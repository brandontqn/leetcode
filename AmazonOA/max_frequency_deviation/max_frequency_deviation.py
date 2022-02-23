"""
ccaabb -> cca or caa or aab or abb -> 1
"""
from collections import defaultdict

def getFrequencyDeviation(s):
    max_freq, min_freq = float("-inf"), float("inf")
    frequencies = defaultdict(int)
    for char in s:
        frequencies[char] += 1
    for value in frequencies.values():
        max_freq = max(max_freq, value)
        min_freq = min(min_freq, value)

    return abs(max_freq - min_freq)

def maxFrequencyDeviation(s):
    n = len(s)
    
    if n < 3:
        return 0

    dp = {}

    max_frequency_deviation = 0
    for i in range(n-1):
        for j in range(i+1, n):
            key = s[i:j]            
            if key not in dp:
                dp[key] = getFrequencyDeviation(s[i:j])            
            frequency_deviation = dp[key]
            max_frequency_deviation = max(max_frequency_deviation, frequency_deviation)
    
    return max_frequency_deviation

def main():
    s = "ccaaaabb"
    result = maxFrequencyDeviation(s)
    print(result)

if __name__ == "__main__":
    main()