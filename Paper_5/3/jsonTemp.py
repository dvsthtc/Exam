import json
import urllib

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'http://python-data.dr-chuck.net/comments_283750.json'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()

#TODO
#Make dictionary from elements in xml file where: key - name, value - count 
jdata = json.loads(data)
nlist = []
for entry in jdata['comments']:
        name = entry.get('name')
        count = entry.get('count')
        nlist.append([name,count])
 
res = dict(nlist)

for i in range(0,len(nlist)):
        print nlist[i][0],nlist[i][1]
       
print 'Dictionary: ',res
