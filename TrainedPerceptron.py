FILENAME = 'data.txt'

class Perceptron:
    input = [[]]
    weight = [[]]
    threshold = []
    output = []
    desiredOutput = []
    v = []
    summation = []

    def get_input(self, input_vectors, inputQty):
        for list in 0, inputQty:
            x=1

class DataAccessObject:
    inputData = []
    desiredOutput = []
    valuesPerVector = None
    inputSize = None

    def __init__(self):
        self.get_data()

    def get_data(self):
        file = open(FILENAME, "r")
        next(file)
        for line in file:
            fields = line.split(" ")
            size = len(fields)
            self.desiredOutput.append(float(fields[0]))
            if not self.inputData:
                for value in range(1, size):
                    self.inputData.append([])
            for value in range(1, size):
                self.inputData[value-1].append(float(fields[value]))


dao = DataAccessObject()
