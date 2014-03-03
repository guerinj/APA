import re as re
import numpy as np
import matplotlib.pyplot as plt

data = []
user_ids = set()
movie_dates = set()
movie_names = set()
notes = list()
reviews_by_users = {}


with open('movie_lens.csv', 'r') as f:
    for line in f:
        user, movie, note = line.strip().split("|")
        data.append({user: user, movie: movie, note: note})

        user_ids.add(user)
        movie_names.add(movie)
        notes.append(int(note))

        if user in reviews_by_users:
            reviews_by_users[user].append(
                {user: user, movie: movie, note: note}
                )
        else:
            reviews_by_users[user] = [{user: user, movie: movie, note: note}]

        date = re.findall(r'\(([0-9]{4})\)', movie)

        if len(date) > 0:
            movie_dates.add(date[0])

print "2.1 ------------------"
print "\tThere are %s reviews in the training set." % len(data)
print "\tThere are %s users in the training set." % len(user_ids)

print "2.2 ------------------"
print "\tThere are %s movies in the training set." % len(movie_names)
print "\tMost recent movie is from %s" % min(movie_dates)
print "\tLeast recent movie is from %s" % max(movie_dates)

print "2.3 ------------------"

plt.hist(notes)
plt.xlabel('Note')
plt.ylabel('Number')
plt.title('Notes distribution')
#plt.show()
print "\t Ploted"

print "2.4 ------------------"
#print "\tMean number of review by user : %s " % np.mean(reviews_by_users[])
#print "\tStandard deviation number of review by user : %s " % np.std(reviews_by_users.values())
print "\tSmallest number of review : %s" % min(reviews_by_users.values())
print "\tHighest number of review : %s" % max(reviews_by_users.values())

print "3.5 ------------------"
print "\tLa corrélation est une mesure de similarité car (...)"

print "3.6 ------------------"
for index, movie in enumerate(movie_names):
    for movie2 in movie_names[(index+1):]:
        movie_vector = 
        movie2_vector = 