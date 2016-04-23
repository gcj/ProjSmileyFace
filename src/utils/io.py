import os
import pickle


def pickle_save(vars_all, fn):
    dirname = os.path.dirname(fn)
    if (dirname != '') and (os.path.isdir(dirname) == False):
        os.makedirs(dirname)
        
    f = open(fn, 'wb')
    pickle.dump(vars_all, f, -1)
    f.close()
    
def pickle_load(fn):
    f = open(fn, 'rb')
    X = pickle.load(f)
    f.close()
    return X
