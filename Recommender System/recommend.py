from pandas import read_csv
from scipy.spatial.distance import euclidean

data_url = 'https://gist.githubusercontent.com/jackbandy/5cd988ab5c3d95b79219364dce7ee5ae/raw/731ecdbecc7b33030f23cd919e6067dfbaf42feb/song-ratings.csv'


ratings=read_csv(data_url,index_col=0)
# print(ratings.head(5))
ratings=ratings.fillna(0)


def distance(person1,person2):
    distance=euclidean(person1,person2)
    return distance


# jack=ratings.loc['Jack']
# nick=ratings.loc['Nick']
# trevor=ratings.loc['Trevor']


# print(distance(jack,nick))
# print(distance(jack,trevor))

def most_similar(name):
    person=ratings.loc[name]
    closest=float('inf')
    closest_person=''
    for other_person in ratings.itertuples():
        if other_person.Index==name:
            continue
        distance_to_other_person=distance(person,ratings.loc[other_person.Index])
        # print(other_person.Index,end=" ")
        # print(distance_to_other_person)
        if distance_to_other_person<closest:
            closest=distance_to_other_person
            closest_person=other_person.Index
    return closest_person

similar=most_similar("Hallie")
print(similar)
name="Hallie"
person=ratings.loc[name]
similar=ratings.loc[similar]
for i in range(0,len(person)):
    if person[i]==0 and similar[i]>=3.0:
        print(ratings.columns[i])
        
