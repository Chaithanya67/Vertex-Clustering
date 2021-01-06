import os 
  

    
path = "./study_cluster"
article_count = 0
country_count = 0
search_count = 0
university_count = 0
facolta_count = 0

for count, filename in enumerate(os.listdir(path)): 
    if(filename[0] == 'a'):
        article_count += 1
        dst = "article_" + str(article_count) + ".html"
    if(filename[0] == 'c'):
        country_count += 1
        dst = "country_" + str(country_count) + ".html"
    if(filename[0] == 's'):
        search_count += 1
        dst = "search_" + str(search_count) + ".html"
    if(filename[0] == 'u'):
        university_count += 1
        dst = "univeristy_" + str(university_count) + ".html"
    if(filename[0] == 'f'):
        facolta_count += 1
        dst = "facoltà_" + str(facolta_count) + ".html"
        
    src ='./study_cluster/'+ filename 
    dst ='./study_cluster_pulito/'+ dst 
    os.rename(src, dst) 
