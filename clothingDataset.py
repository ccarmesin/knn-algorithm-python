import pandas as pandas
import random

def readExcelFile(file):

    # Replace backslash with normal slash
    file = file.replace('\\','/')

    # Read an excel file from a given path
    df = pandas.read_excel(file)

    sizes = []

    for size in df.columns:

        # Skip the first column
        if(size == "International"):
            continue

        chestLength = df[size][0].split("–")
        bodyLength = df[size][3].split("–")

        sizeConfig = {
            "clothingSize": size,
            "bodyLengthMin": int(bodyLength[0]),
            "bodyLengthMax": int(bodyLength[1]),
            "chestLengthMin": int(chestLength[0]),
            "chestLengthMax": int(chestLength[1])
        }

        sizes.append(sizeConfig)

    return sizes

def createDatapoits(config, sizes):

    datapointsPerSize = int(config.get("total") / len(sizes))
    dataset = []
    colors = ["g", "r", "c", "m", "y", "k"]

    for size in sizes:

        sizeColor = colors[random.randint(0, len(colors) - 1)]

        for x in range(datapointsPerSize):

            # Generate random points
            x = random.uniform(size.get("bodyLengthMin"), size.get("bodyLengthMax"))
            y = random.uniform(size.get("chestLengthMin"), size.get("chestLengthMax"))
            label = size.get("clothingSize")

            datapoint = {
                "x": x,
                "y": y,
                "label": label,
                "color": sizeColor
            }

            dataset.append(datapoint)

    return dataset

def shuffle(dataset):

    return random.shuffle(dataset)

def loadClothingSizeDataset(config):

    sizes = readExcelFile(config.get("file"))
    dataset = createDatapoits(config, sizes)
    shuffle(dataset)

    #Split index by given ratio
    splitIndex = int(len(dataset) * config.get("trainTestRatio"))

    return [
        dataset[:splitIndex], dataset[splitIndex:]
    ]