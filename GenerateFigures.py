#
#   @file : GenerateFigures.py
#   @date : 17 April 2024
#   @authors : Orel Adivi and Daniel Noor
#
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

BASE_DIRECTORY = './artifacts'


def generate_figure1() -> None:
    """This function generates a figure for experiment #1."""
    lengths = []
    with open(BASE_DIRECTORY + '/experiment1.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        label_line = reader.__next__()
        assert label_line[0] == 'length'
        labels = [label[:-12] for label in label_line[1::2]]
        values = [[] for _ in range(len(labels))]
        for row in reader:
            lengths.append(int(row[0]))
            current_values = row[1::2]
            for i in range(len(current_values)):
                values[i].append(int(current_values[i]))

    assert len(labels) == len(values)
    lengths = np.array(lengths)
    values = [np.array(arr) for arr in values]

    plt.figure(figsize=(7, 5))
    for i in range(len(labels)):
        plt.plot(lengths, values[i], label=labels[i])

    print('=== Generating figure #1... ===')
    plt.title('Deletion correction capabilities of different codes')
    plt.xlabel('Codeword length [bit]')
    plt.ylabel('Maximal number of fixable deletions [bit]')
    plt.xlim([lengths[0], lengths[-1]])
    plt.ylim([0, 50 * int(np.ceil(max([np.max(arr) for arr in values]) / 50.0))])
    plt.xticks(np.arange(lengths[0], lengths[-1] + 1, 50))
    plt.yticks(np.arange(0, 50 * int(np.ceil(max([np.max(arr) for arr in values]) / 50.0)) + 1, 25))
    plt.legend()
    plt.grid()
    plt.savefig(BASE_DIRECTORY + '/figure1.png', format='png', dpi=300)


def generate_figure2() -> None:
    """This function generates a figure for experiment #2."""
    lengths = []
    with open(BASE_DIRECTORY + '/experiment2.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        label_line = reader.__next__()
        assert label_line[0] == 'length'
        labels = [label[:-12] for label in label_line[1::3]]
        values = [[] for _ in range(len(labels))]
        for row in reader:
            lengths.append(int(row[0]))
            current_values = row[1::3]
            for i in range(len(current_values)):
                values[i].append(int(current_values[i]))

    assert len(labels) == len(values)
    lengths = np.array(lengths)
    values = [np.array(arr) for arr in values]

    plt.figure(figsize=(7, 5))
    for i in range(len(labels) - 1):
        plt.plot(lengths, values[i], label=labels[i])
    plt.plot(lengths, values[-1], '--', color='black', label=labels[-1])

    print('=== Generating figure #2... ===')
    plt.title('Deletion correction capabilities of codes that generate less codewords than the desired')
    plt.xlabel('Codeword length [bit]')
    plt.ylabel('Maximal number of fixable deletions [bit]')
    plt.xlim([lengths[0], lengths[-1]])
    plt.ylim([0, 50 * int(np.ceil(max([np.max(arr) for arr in values]) / 50.0))])
    plt.xticks(np.arange(lengths[0], lengths[-1] + 1, 50))
    plt.yticks(np.arange(0, 50 * int(np.ceil(max([np.max(arr) for arr in values]) / 50.0)) + 1, 25))
    plt.legend()
    plt.grid()
    plt.savefig(BASE_DIRECTORY + '/figure2.png', format='png', dpi=300)


def generate_graph4():
    return
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


def generate_graph3():
    return
    x = []
    ys = []
    with open('artifacts/experiment3.csv', newline='') as csvfile:
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

    labels = ['2', '4', '8']
    labels = ['q=' + label for label in labels]
    for y, label in zip(ys, labels):
        plt.plot(x, y, label=label)
    plt.title("VTRepetitionNaryCode with Different Bases")
    plt.xlabel("Code Length [bit]")
    plt.ylabel("Maximum Number of Fixable Deletions [bit]")
    plt.legend()
    plt.grid()
    plt.savefig("artifacts/graph4.png")


if __name__ == "__main__":
    FIGURE_ID = None
    if len(sys.argv) > 1:
        FIGURE_ID = int(sys.argv[-1])
    if FIGURE_ID is None or FIGURE_ID == 1:
        generate_figure1()
    if FIGURE_ID is None or FIGURE_ID == 2:
        generate_figure2()
    if FIGURE_ID is None or FIGURE_ID == 3:
        generate_graph3()
    if FIGURE_ID is None or FIGURE_ID == 4:
        generate_graph4()
