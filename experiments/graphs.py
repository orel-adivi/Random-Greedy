import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = [100, 200, 300, 400, 500]

    y1 = [9, 24, 27, 39, 51]
    y2 = [9, 29, 35, 51, 67]
    y3 = [4, 8, 13, 14, 31]
    y4 = [13, 31, 46, 64, 81]
    y5 = [38, 83, 129, 169, 215]

    plt.plot(x, y1, label='Repetition Code')
    plt.plot(x, y2, label='VT Repetition Code')
    plt.plot(x, y3, label='N-ary VT Repetition Code')
    plt.plot(x, y4, label='Random Code')
    plt.plot(x, y5, label='Greedy Random Code')
    plt.title("Deletion Correction Capabilities of Different Codes")
    plt.xlabel("Code Length [bit]")
    plt.ylabel("Maximum Number of Fixable Deletions [bit]")
    plt.legend()
    plt.grid()
    plt.savefig("graph.png")
