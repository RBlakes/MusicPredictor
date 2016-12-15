# builds a neural network and uses the attribute values
# as the inputs for the neural network, uses the last
# attribute value as the output, in this case it is hotness
# this neural network uses a supervised data set

from pybrain.datasets.supervised import SupervisedDataSet
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer


# Remember to change the number based on how many attributes there are
# using all the attributes has 13, using a combination of the attributes
# minus one has 12
dataset = SupervisedDataSet(12,1)

fileReader = open('musicdataconvertedB13.csv', 'r')

for line in fileReader.readlines():
    data = [float(x) for x in line.strip().split(',') if x != '']
    indata = tuple(data[:12])
    outdata = tuple(data[12:])
    dataset.addSample(indata,outdata)

n = buildNetwork(dataset.indim,8,8,dataset.outdim,bias=True)
t = BackpropTrainer(n,learningrate=0.01,momentum=0.5,verbose=True)
t.trainOnDataset(dataset,20)
#t.testOnData(verbose=True)




