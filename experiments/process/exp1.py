if __name__ == "__main__":
    y1 = [calculate_max_deletions(lambda: RepetitionCode(length)) for length in range(100, 600, 100)]
    print(y1)
    y2 = [calculate_max_deletions(lambda: VTRepetitionCode(length, calculate_m(length)))
          for length in range(100, 600, 100)]
    print(y2)
    y3 = [calculate_max_deletions(lambda: VTRepetitionNaryCode(length, calculate_m(length)))
          for length in range(100, 600, 100)]
    print(y3)
    y4 = [calculate_max_deletions(lambda: RandomCode(length)) for length in range(100, 600, 100)]
    print(y4)
    y5 = [calculate_max_deletions(lambda: GreedyRandomCode(length)) for length in range(100, 600, 100)]
    print(y5)
    y6 = [calculate_max_deletions(lambda: GreedyCode(length)) for length in range(100, 600, 100)]
    print(y6)

if __name__ == "__main__":
    y1 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=2)) for length in range(100, 600, 100)]
    print(y1)
    y2 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=3)) for length in range(100, 600, 100)]
    print(y2)
    y3 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=4)) for length in range(100, 600, 100)]
    print(y3)
    y4 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=5)) for length in range(100, 600, 100)]
    print(y4)
