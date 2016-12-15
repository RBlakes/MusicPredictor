# builds a neural network and uses the attribute values
# as the inputs for the neural network, uses the last
# attribute value as the output, in this case it is hotness
# this neural network uses a classification data set

from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

# Remember to change the number based on how many attributes there are
# using all the attributes has 13, using a combination of the attributes
# minus one has 12
dataset = ClassificationDataSet(13,1)

fileReader = open('musicdataconvertedBAll.csv', 'r')

for line in fileReader.readlines():
    data = [float(x) for x in line.strip().split(',') if x != '']
    indata = tuple(data[:13])
    outdata = tuple(data[13:])
    dataset.addSample(indata,outdata)

testdata, traindata = dataset.splitWithProportion( 0.25 )


print traindata['input'], traindata['target'], testdata.indim, testdata.outdim

neuralnetwork = buildNetwork( traindata.indim, 13, traindata.outdim)
trainer = BackpropTrainer(neuralnetwork, dataset=traindata, momentum=0.1, learningrate=0.01, verbose=True, weightdecay=0.01)

trainer.trainEpochs(20)
testresult = percentError(trainer.testOnClassData( dataset=testdata), testdata['class'])
print 'Percent Error on Test dataset: %5.2f%%' % testresult


