import pandas as pd
#import numpy as np
from pushbullet import Pushbullet 

title = 0
website = 1
phoneNumber = 2

#read csv file
data = pd.read_csv (r'results.csv')

#extract the info I care about 
df = pd.DataFrame(data, columns= ['title','website','phoneNumber'])

#replace NaN with a "0" to make it easier to handle
#df.fillna(0)
#df.replace(np.nan,0)

# For some reason it only works if I do it for every column
df['title'] = df['title'].fillna(0)
df['website'] = df['website'].fillna(0)
df['phoneNumber'] = df['phoneNumber'].fillna(0)

# get specific thing  
#a = df.loc[[1], ["website"]]

# turn df into dictionary 
clients = df.to_numpy()

#print(clients)
# clients[row, column] ## how it werks 

pb = Pushbullet("o.ILvrcOc81yC3Vpmey8xClx9JTxAx9WMz") # access token to log me in 
device = pb.devices[0]

a = len(clients) # get how many clients I have 
for i in range(a): 
    if clients[i, phoneNumber] == 0:
#        print("no phone")
        continue
    elif clients[i, website] == 0:
#        print("no website")
        continue
    elif clients[i, title] == 0:
#        print("no title")
        name = "!\n"
    else:
        name = " "+clients[i, title]+"!\n"
    number = clients[i, phoneNumber]
    site = clients[i, website]
    message = "Hej"+name+"\n"+"Jag hittade er hemsida "+site+" och såg att det var ett antal problem med den. Jag kan skicka en rapport av vad jag har hittat och fixa ett problem gratis i förhoppning om att vi gör affärrer i framtiden."+"\n\nMvh Julius"
    push = pb.push_sms(device, number, message)
    print(name+" "+number+" "+site)
