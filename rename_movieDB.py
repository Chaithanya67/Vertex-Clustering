import os 
  
path = "./movieDB_cluster"
discuss_count = 0
movie_count = 0
person_count = 0
tv_count = 0
user_count = 0

for count, filename in enumerate(os.listdir(path)): 
    if(filename[0] == 'd'):
        discuss_count += 1
        dst = "discuss_" + str(discuss_count) + ".html"
    if(filename[0] == 'm'):
        movie_count += 1
        dst = "movie_" + str(movie_count) + ".html"
    if(filename[0] == 'p'):
        person_count += 1
        dst = "person_" + str(person_count) + ".html"
    if(filename[0] == 't'):
        tv_count += 1
        dst = "tv_" + str(tv_count) + ".html"
    if(filename[0] == 'u'):
        user_count += 1
        dst = "user_" + str(user_count) + ".html"
        
    src ='./movieDB_cluster/'+ filename 
    dst ='./movieDB_cluster_pulito/'+ dst 
    os.rename(src, dst) 