#
#   @file : GenerateFigures.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
import matplotlib.pyplot as plt
import csv


def generate_graph1():
    labels = []
    x = []
    ys = []
    with open('../experiments/artifacts/experiment1_results.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        start = True
        for row in reader:
            if start:
                labels = [elem[1:] for elem in ','.join(row).split(',')][1::4]
                start = False
                ys = [[] for _ in labels]
            else:
                row = ','.join(row).split(',')
                x.append(int(row[0]))
                values = row[1::2]
                for y, val in zip(ys, values):
                    y.append(int(val))

    labels.append('GreedyCode')
    ys.append([9, 34, 62, 79, 50, 83, 78, 110, 98, 98])
    for y, label in zip(ys, labels):
        plt.plot(x, y, label=label)
    plt.title("Deletion Correction Capabilities of Different Codes")
    plt.xlabel("Code Length [bit]")
    plt.ylabel("Maximum Number of Fixable Deletions [bit]")
    plt.legend()
    plt.grid()
    plt.savefig("artifacts/graph1.png")


def generate_graph2():
    labels = []
    x = []
    ys = []
    with open('../experiments/artifacts/experiment3_results.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        start = True
        for row in reader:
            if start:
                labels = [elem[1:] for elem in ','.join(row).split(',')][1::6]
                start = False
                ys = [[] for _ in labels]
            else:
                row = ','.join(row).split(',')
                x.append(int(row[0]))
                values = row[1::3]
                for y, val in zip(ys, values):
                    y.append(int(val))

    for y, label in zip(ys, labels):
        plt.plot(x, y, label=label)
    plt.title("Deletion Correction Capabilities of Linspace/Logspace Codes")
    plt.xlabel("Code Length [bit]")
    plt.ylabel("Maximum Number of Fixable Deletions [bit]")
    plt.legend()
    plt.grid()
    plt.savefig("artifacts/graph2.png")


def generate_graph3():
    x = []
    ys = []
    with open('../experiments/artifacts/experiment4_results.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        start = True
        for row in reader:
            row = ','.join(row).split(',')
            if start:
                start = False
                ys = [[] for _ in row][1::4]
            else:
                x.append(int(row[0]))
                values = row[1::2]
                for y, val in zip(ys, values):
                    y.append(int(val))

    labels = ['2', '3', '4', '5']
    labels = ['options=' + label for label in labels]
    for y, label in zip(ys, labels):
        plt.plot(x, y, label=label)
    plt.title("RandomGreedyCode with Different Parameters")
    plt.xlabel("Code Length [bit]")
    plt.ylabel("Maximum Number of Fixable Deletions [bit]")
    plt.legend()
    plt.grid()
    plt.savefig("artifacts/graph3.png")


if __name__ == "__main__":
    # generate_graph1()
    # generate_graph2()
    generate_graph3()

