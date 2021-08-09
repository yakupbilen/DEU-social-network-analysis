# If links are the same, then one will be deleted
# Example = deu.edu.tr - deu.edu.tr/

links = []
with open("all_links.txt",'r') as file:
    links = file.readlines()

clear_links = []
bool = False
for i in range(len(links)):
    bool = False
    for j in range(i+1,len(links)):
        if(links[i].strip("\n").replace(":","").replace("/","").replace("\n","")==links[j].strip('\n').replace(":","").replace("/","").replace("\n","")):
            bool=True
            break
    if(bool==False):
        clear_links.append(links[i])

with open("clean_links.txt","w") as file:
    for link in clear_links:
        file.write(link)
