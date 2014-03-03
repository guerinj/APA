import numpy as np
from scipy.optimize import fmin_l_bfgs_b
import math
data = []
REPUBLICAN = -1
DEMOCRAT = 1

mapping = {"y": 1, "n": -1, "?": 0}

with open('house-votes-84.data', 'r') as f:
    for line in f:
        raw = line.strip().split(',')
        tmp = {
            "etiquette": REPUBLICAN if raw[0] == "republican" else DEMOCRAT,
            "observation": np.array([mapping[r] for r in raw[1:]] + [1])
        }
        print(tmp)
        # for i, v in enumerate(tmp["observation"]):
        #     if v == 'y':
        #         tmp["observation"][i] = 1
        #     elif v == 'n':
        #         tmp["observation"][i] = -1
        #     else:
        #         tmp["observation"][i] = 0
        # tmp["observation"].append(1)

        data.append(tmp)


def classify(w, d):
    return math.copysign(1, np.dot(w, d))


def test(data, w):
    err = 0
    for d in data:
        if classify(w, d["observation"]) * d["etiquette"] < 0:
            err += 1
    print "Errors : %s" % err
    print "Error rate : %s %%" % str((err*100.0/len(data)))[:4]


def f_builder(w, data):
    t = 0
    for d in data:
        t += max(0, 1 - d["etiquette"] * np.dot(w, d["observation"]))
    return t


def fprime_builder(w, data):
    def fprime(w):
        gradient = np.zeros(17)
        for d in data:
            if np.dot(w, d["observation"]) * d["etiquette"] > 1:
                pass
            else:
                gradient += - d["etiquette"] * d["observation"]
                #t.append(-np.dot(w, d["observation"]))
        return gradient
    return np.array(fprime(w))

w_test = [25, -12, 67, -104, -43, 46, -18, -10, 45, -33, 54, -39, 43, -19, 5, -2, 55]

w0 = np.array([1] * 17)


print "Using vector : %s" % w_test
test(data, w_test)

print"\nNow learnning..."

w_calc, f_calc, d = fmin_l_bfgs_b(f_builder, w0, fprime_builder, [data])

print d
print "Using vector : %s" % w_calc
test(data, w_calc)