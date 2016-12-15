# MusicPredictor
Final project for CS 5600.  Uses a neural network to predict how popular a song will be.

## Introduction

The amount of music that is in the world today is incredibly large and continues to grow at a rapid pace.  Not all of this music is worth listening to, however, with most of it never becoming widely listened to.
How do you decide which songs to spend your time listening to?  Listening to each one at least once would take a lifetime.  It also wouldn't be an entirely pleasant experience for you either, as the majority of the songs you wouldn't find enjoyable.
The most efficient use of your time would be to only listen to the songs that would bring you the maximal enjoyment.  To that end this project aims to use a neural network to predict whether or not a song will be popular, and therefore worth listening to.

## Method
Each song has multiple characteristics associated with it that define how it sounds.  This project uses machine learning in the form of a neural network to use these characteristics to determine how positively a song will be received by listeners.  First, attributes for songs are gathered to be used as inputs into the neural network.  A multilayer feed-forward neural network was chosen.  This network takes the inputs in the first layer, combines them using a weighted linear combination then passes that output to the hidden layer.  The hidden layer then uses a nonlinear sigmoid function on the outputs of the first layer to produce the final output.

The output in this case is a number between 0 and 1 that corresponds to an estimation of how "hot" or popular the song will be.  With 1 being the most popular and 0 being the least.  In the data this estimation was made by the echo nest, which is a music classifying application.

A 10k subset from the Million Song Dataset was obtained from the Laboratory for the Recognition and Organization of Speech and Audio(http://labrosa.ee.columbia.edu/millionsong/).  This dataset contains 54 different attributes associated with each song.  For this project 13 of those attributes were chosen to be used.

(add chosen attributes)

First the neural network was trained and tested using all 13 chosen attributes.  Then the neural network was trained and tested with all of the attributes minus one to see if removing one attribute had any effect on the accuracy of the prediction.

## Results and Conclusions

(add graph of results)

It was found that the neural network was able to very accurately predict how popular a song would be given all the attributes.  Also, the removal of a single attribute had very little effect on the accuracy of the prediction.  The removal of the key and mode attribute had the greatest impact on accuracy although this was still within 2% of the accuracy with all the attributes.  This means that if a song is taken and these attributes are obtained for it, it is possible to predict how popular the song will be.

As a continuation of this project it would be interesting to remove different combinations of attributes and test what effect it has on the accuracy of the prediction.  This wasn't done due to the number of combinations of attributes being too large to test thoroughly in the time available.  This would be useful because then the minimum number of attributes needed to accurately predict the popularity of a song would be known.

## Resources:

- http://labrosa.ee.columbia.edu/millionsong/
- https://github.com/tbertinmahieux/MSongsDB/tree/master/PythonSrc
    - hdf5\_getters.py is a direct copy straight from [https://github.com/tbertinmahieux/MSongsDB/blob/408393766dfa449da90faaf8a65aed9cc420849a/PythonSrc/hdf5_getters.py](https://github.com/tbertinmahieux/MSongsDB/blob/408393766dfa449da90faaf8a65aed9cc420849a/PythonSrc/hdf5_getters.py)
- https://github.com/rcrdclub/mm-songs-db-tools
    - mmsongsdbtocsvconverter.py is a direct copy straight from [https://github.com/rcrdclub/mm-songs-db-tools/blob/master/mmsongsdbtools/mmsongsdbtocsvconverter.py](https://github.com/rcrdclub/mm-songs-db-tools/blob/master/mmsongsdbtools/mmsongsdbtocsvconverter.py)
- [pybrain](http://pybrain.org/) : for the neural network
