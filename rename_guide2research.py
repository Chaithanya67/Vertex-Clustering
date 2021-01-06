import os 
  

    
path = "./guide2research_5cluster"
conference_count = 0
journal_count = 0
research_count = 0
special_issue_count = 0
user_count = 0

for count, filename in enumerate(os.listdir(path)): 
    if(filename[0] == 'c'):
        conference_count += 1
        dst = "conference_" + str(conference_count) + ".html"
    if(filename[0] == 'j'):
        journal_count += 1
        dst = "journal_" + str(journal_count) + ".html"
    if(filename[0] == 'r'):
        research_count += 1
        dst = "research_" + str(research_count) + ".html"
    if(filename[0] == 's'):
        special_issue_count += 1
        dst = "special_issue_" + str(special_issue_count) + ".html"
    if(filename[0] == 'u'):
        user_count += 1
        dst = "user_" + str(user_count) + ".html"
        
    src ='./guide2research_5cluster/'+ filename 
    dst ='./guide2research_5cluster_pulito/'+ dst 
    os.rename(src, dst) 
