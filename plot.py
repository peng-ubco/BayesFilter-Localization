import matplotlib.pyplot as plt
import numpy as np


def create_poles(poles, distance):
    x = range(distance)
    y = np.zeros(distance)
    plt.ylim([0., 1.0])
    # plt.scatter(x, y, marker='s', s=40, c='r')
    plt.bar(x, [0.05]*len(y), width=0.6, color=('red'))
    plt.bar(poles, [0.7]*len(poles), width=1.0, color=('red'))
    plt.title('Environment', loc='left')


def plot_poles(poles, distance):
    plt.subplot(311)
    plt.yticks([])
    plt.xticks([])
    plt.xlim([-0.9, distance + 0.9])
    create_poles(poles, distance)
    plt.title('Environment', loc='left')


def plot_belief(y, distance):
    plt.subplot(312)
    plt.yticks([])
    plt.ylim(0., 1.2)
    plt.xlim([-0.9, distance + 0.9])
    plt.bar([0, distance], [0, 0], color='blue')
    x = range(distance)
    for i in range(distance):
        plt.bar([i, i], [0, y[i]], color='blue')
    plt.title('Update Belief', loc='left')


def plot_current_measurement(loc, poles, distance):
    plt.subplot(313)
    plt.yticks([])
    plt.xticks([])
    plt.xlim([loc - 5.0, loc + 5.0])
    # plt.ylim([0., 1.0])

    plt.plot([loc + 0.2], [0.5], 'g<', markersize=30, alpha=0.5)
    plt.plot([loc], [0.45], 'bo', markersize=30)
    plt.plot([loc], [0.1], 'bs', markersize=30)
    create_poles(poles, distance)
    plt.title('Robot Surrounding Zoom In', loc='left')


def plot(distance, poles, P_loc_i_posterior, robot, block=False, pause_time=1, filename='0'):
    if robot.pole_detected(poles):
        block = False
    plot_poles(poles, distance)
    plot_belief(P_loc_i_posterior, distance)
    plot_current_measurement(robot.pos, poles, distance)
    plt.tight_layout(pad=0.5)
    plt.savefig(filename)
    if block:
        plt.show()
    else:
        plt.pause(0.1)
        plt.show(block=block)
        plt.pause(pause_time)
        plt.close()
