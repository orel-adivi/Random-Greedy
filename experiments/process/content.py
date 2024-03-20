if __name__ == "__main__":
    y1 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=2)) for length in range(100, 600, 100)]
    print(y1)
    y2 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=3)) for length in range(100, 600, 100)]
    print(y2)
    y3 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=4)) for length in range(100, 600, 100)]
    print(y3)
    y4 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=5)) for length in range(100, 600, 100)]
    print(y4)

if __name__ == "__main__":
    print(longest_common_subsequence("111", "000"))
    print(longest_common_subsequence("10101", "10010"))
