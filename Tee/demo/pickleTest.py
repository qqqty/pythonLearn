import pickle

data = pickle.load(open('sourse/banner.p', 'rb'))


for item in data:
    res = "".join([i[1] * i[0] for i in item])
    print res