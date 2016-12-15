import os
import sys
import time
import datetime


# path to the Million Song Dataset subset (uncompressed)
# make sure to change the path to wherever it is located
msd_subset_path = 'C:\Users\Randy\Desktop\MillionSongSubset'
msd_subset_data_path = os.path.join(msd_subset_path, 'data')
msd_subset_addf_path = os.path.join(msd_subset_path, 'AdditionalFiles')
assert os.path.isdir(msd_subset_path), 'wrong path'  # sanity check
# path to the Million Song Dataset code
# make sure to change the path to wherever it is located
msd_code_path = 'C:\Users\Randy\Desktop\MSongsDB'
assert os.path.isdir(msd_code_path), 'wrong path'  # sanity check
# we add some paths to python so we can import MSD code
sys.path.append(os.path.join(msd_code_path, 'PythonSrc'))

# import code to convert the fdh5 files to cvs files
from mmsongsdbtools.mmsongsdbtocsvconverter import MMSongsDbToCsvConverter


# the following function simply gives us a nice string for
# a time lag in seconds
def strtimedelta(starttime, stoptime):
    return str(datetime.timedelta(seconds=stoptime - starttime))

# converts the files in the MillionSongSubset to cvs files
# and measures how long it takes
# takes about 20 min to convert all the songs in the A folder
# so does the top A and B folders seperately

#t1 = time.time()
#converterA = MMSongsDbToCsvConverter('musicdataconvertedA.csv', ['title', 'artist_name', 'artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
#converterA.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\A')
#t2 = time.time()
#print 'Song A data extracted in:', strtimedelta(t1, t2)

#t3 = time.time()
#converterB = MMSongsDbToCsvConverter('musicdataconvertedB.csv', ['title', 'artist_name', 'artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
#converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
#t4 = time.time()
#print 'Song B data extracted in:', strtimedelta(t3, t4)

# for the purposes of testing the accuracy of a prediction
# only the main folder B was used due to it being slightly
# smaller than A
# this gets some attributes from B, first all of them
# then gets all of them minus one, then all minus a different one
# until each combination of attributes is used
t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedBAll.csv', ['artist_hotttnesss', 'duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B1 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB1.csv', ['duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B1 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB2.csv', ['artist_hotttnesss', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B2 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB3.csv', ['artist_hotttnesss','duration', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B3 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB4.csv', ['artist_hotttnesss','duration', 'end_of_fade_in', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B4 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB5.csv', ['artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B5 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB6.csv', ['artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'key_confidence', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B6 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB7.csv', ['artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B7 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB8.csv', ['artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B8 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB9.csv', ['artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B9 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB10.csv', ['artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'time_signature', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B10 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB11.csv', ['artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature_confidence', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B11 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB12.csv', ['artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'year', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B12 data extracted in:', strtimedelta(t1, t2)

t1 = time.time()
converterB = MMSongsDbToCsvConverter('musicdataconvertedB13.csv', ['artist_hotttnesss','duration', 'end_of_fade_in', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'tempo', 'start_of_fade_out', 'time_signature', 'time_signature_confidence', 'song_hotttnesss'])
converterB.convert_directory('C:\Users\Randy\Desktop\MillionSongSubset\data\B')
t2 = time.time()
print 'Song B13 data extracted in:', strtimedelta(t1, t2)
