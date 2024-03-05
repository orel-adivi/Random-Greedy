


if __name__ == "__main__":
    l = 400
    log_l = int(np.ceil(np.log2(l)))
    m = log_l + int(np.ceil(np.log2(log_l))) + 1
    r = VTRepetitionNaryCode(l, m)
    print(len(r.codewords))
    print(r.max_deletions())


if __name__ == "__main__":
    l = 400
    log_l = int(np.ceil(np.log2(l)))
    m = log_l + int(np.ceil(np.log2(log_l))) + 1
    r = VTRepetitionCode(l, m)
    print(len(r.codewords))
    print(r.max_deletions())

if __name__ == "__main__":
    r = RepetitionCode(400)
    # print(r.codewords)
    print(r.max_deletions())

if __name__ == "__main__":
    r = GreedyRandomCode(400, options=3)
    print(r.codewords)
    print(r.max_deletions())

if __name__ == "__main__":
    r = RandomCode(400)
    print(r.codewords)
    print(r.max_deletions())

if __name__ == "__main__":
    r = LogSpaceCode(100)
    print(r.codewords)
    print(r.max_deletions())
    print(r.decode(r.mapping[3][0:75]))

if __name__ == "__main__":
    r = LinSpaceCode(100)
    print(r.codewords)
    print(r.max_deletions())
    print(r.decode(r.mapping[3][0:80]))

if __name__ == "__main__":
    r = GreedyCode(200)
    print(r.codewords)
    print(r.max_deletions())

if __name__ == "__main__":
    print(longest_common_subsequence("111", "000"))
    print(longest_common_subsequence("10101", "10010"))
