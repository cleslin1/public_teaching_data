import json
import pickle
import time

start = time.time()
with open('ensemblData.json') as json_file:
    data = json.load(json_file)
print("Time spent loading JSON:  {0:.3f} sec".format(time.time() - start))
print(len(data.keys()))
print(data['5S_rRNA']['00000201285']['biotype'])



start = time.time()
with open("ensemblData.pkl", "wb") as out_fh:
    pickle.dump(data, out_fh, pickle.HIGHEST_PROTOCOL )
print("Time spent dumping Python:  {0:.3f} sec".format(time.time() - start))


start = time.time()
with open("ensemblData.pkl", "rb") as in_fh:
    ensembl = pickle.load(in_fh)
print("Time spent loading into Python:  {0:.3f} sec".format(time.time() - start))
print(len(ensembl.keys()))
print(ensembl['5S_rRNA']['00000201285']['biotype'])