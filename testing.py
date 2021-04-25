import pickle

dic = {}

try:
    dataids = open("dataid.dat", "wb")
    pickle.dump(dic, dataids)
    dataids.close()
except Exception as e:
    print(e)
    dataids.close()





