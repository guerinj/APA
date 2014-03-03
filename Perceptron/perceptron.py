import cPickle, gzip, numpy, random
import numpy as np
import matplotlib.pyplot as plt
# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()


#
#  1. Analyse du corpus
#

print "1.2 La dimension des images est 28x28"

print "1.3 Nombre d'images disponibles, "
print "\t pour les tests : %s"  % test_set[0].shape[0]
print "\t pour l'apprentissage : %s"  % train_set[0].shape[0]

print "1.4 Les valeurs des pixels vont de 0 a 1."


#
#  2. Perceptron : premiers pas
#

train_size = 1000
trained_target = 7
train_order = range(train_size)
random.shuffle(train_order)
classifier = np.zeros((784))

print "2.5 Ordre d'apprentissage : "
print train_order[:10]



print "2.6 Fonction pas d'apprentissage"

def train_step(image, classifier, image_class):
	y = np.dot(image, classifier)
	
	if y*image_class > 0 :
		return False, classifier
	else:
		return True, np.add(classifier, image * image_class)



print "2.7 Fonction epoque d'apprentissage"

def train_epoch(train_set, trained_target, order, classifier):
	train_classifier = classifier
	updates = 0

	for index in order:
		changed, train_classifier = train_step(
			train_set[0][index],
			train_classifier,
			1 if trained_target == train_set[1][index] else -1
			)
		
		if changed:
			updates +=1
	
	return train_classifier, updates

print "2.8 Fonction de test"


def test_classifier(test_set, classifier, target):
	error = 0
	success = 0
	for index, image in enumerate(test_set[0]):
		result = np.dot(classifier, image)
		label = 1 if test_set[1][index] == target else -1

		if result*label > 0:
			success += 1
		else:
			error +=1

	print "Test effectues : %s/%s erreurs soit %s pourcent" % (error, success+error, error*100.0/(success+error) )
	return error, success

print "Test des fonctions precedentes :"

small_train_set = [
	train_set[0][:train_size],
	train_set[1][:train_size]
	]

small_test_set = [
	test_set[0][:train_size],
	test_set[1][:train_size]
	]	

results = [[0] * 10, [0] * 10, [0] * 10]
for target  in range(10):
	result = []
	print "\n\n\n"
	print "Apprentissage pour %s" % target
	print "1er passage"
	classifier, updates = train_epoch(small_train_set, target, train_order, classifier)
	e, s = test_classifier(small_train_set, classifier, target)

	print "2eme passage"
	random.shuffle(train_order)
	classifier, updates = train_epoch(small_train_set, target, train_order, classifier)
	e, s = test_classifier(small_train_set, classifier, target)

	print "3eme passage"
	random.shuffle(train_order)
	classifier, updates = train_epoch(small_train_set, target, train_order, classifier)
	e, s = test_classifier(small_train_set, classifier, target)

	


print "Classifier obtenu : "
print classifier[:10]



