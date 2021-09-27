
# import urllib library
from urllib.request import urlopen
import pandas as pd
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://dblp.org/search/publ/api?format=json&q=piyush%20rai"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response

results = data_json['result']['hits']

out = []
for i in range(len(results)):
    try:
        for hit in results['hit']:
            #print(hit['info'])
            tmp = hit['info']
            author_list = []
            for i in tmp['authors']['author']:
                author_list.append(i['text'])
            tmp['authors'] = ",".join(author_list)
            
            out.append(tmp)
    except:
         pass
    
    
    
df = pd.DataFrame(out)
df.to_csv('piyush_rai_pubs.csv')