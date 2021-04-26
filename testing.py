import pickle
import json

dic = {"asff":2356,"ef3qd":"23rer"}

try:
    dataids = open("clusterdata\\dataddddd.json", "w")
    dataa = json.dump(dic, dataids)
    print(dataa)
    dataids.close()
except Exception as e:
    print(dataa)
    print(e)
    dataids.close()
