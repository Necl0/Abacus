import bz2
import pickle
import _pickle as cPickle

#compress pickle file
def compress_pickle(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w') as f:
        cPickle.dump(data, f)



#load model.pkl and compress
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

compress_pickle('model', model)
