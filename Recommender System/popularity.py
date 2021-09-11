import pandas
from sklearn.model_selection import train_test_split
import Recommenders
triplets_file = './triplets_file/triplets_file.csv'
songs_metadata_file = './song_data/song_data.csv'


song_df_1=pandas.read_csv(triplets_file)
song_df_2=pandas.read_csv(songs_metadata_file)

# song_df_1.columns = ['user_id', 'song_id', 'listen_count']
song_df=pandas.merge(song_df_1,song_df_2.drop_duplicates(['song_id']),on="song_id",how="left")

song_grouped=song_df.groupby(['title']).agg({'listen_count':'count'}).reset_index()


grouped_sum=song_grouped['listen_count'].sum()
song_grouped['percentage']  = song_grouped['listen_count'].div(grouped_sum)*100
song_grouped=song_grouped.sort_values(['listen_count', 'title'],ascending=[0,1])
print(song_grouped['title'].head(5))

# users=song_df['user_id'].unique()
# songs=song_df['user_id'].unique()

# train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)

# pm=Recommenders.popularity_recommender_py()
# pm.create(train_data,'user_id','song')

# user_id=users[5]
# print(pm.recommend(user_id))