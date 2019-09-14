import matplotlib.pyplot as plt

def drawFigure(trainSet, testPoint):

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Add trainSet to scatter
    for datapoint in trainSet:
        ax.scatter(datapoint["x"], datapoint["y"], color=datapoint.get("color"), s=10)

    # Add testPoint to scatter
    ax.scatter(testPoint.get("x"), testPoint.get("y"), color="#0000ff", s=20)
    ax.set_xlabel('bodyLength')
    ax.set_ylabel('chestLength')
    plt.show()