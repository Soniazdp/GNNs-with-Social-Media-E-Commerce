import json
import csv

# convert json to csv
with open('data/output.json', "r") as f:
    data = json.load(f)

output_dict = {}
info_dict = {}
count = {}

for post in data:
    for h in post['hashtags']:
        if h not in count:
            count[h] = 0
        count[h] += 1
        
# print the most popular hashtags
top_count = sorted(count.items(), key=lambda x: x[1], reverse=True)[:3]
top_h = [x[0] for x in top_count]

for post in data:
    for h in post['hashtags']:
        if h not in output_dict:
            output_dict[h] = set()
            info_dict[h] = set()
        # add other hashtags to the list except the one we are looking for
        output_dict[h].update(set(x for x in post['hashtags'] if x != h))
        info_dict[h].add((post['id'], post['url'], post['likesCount'], post['ownerUsername'], post['caption'], post['timestamp']))

# # write about the most popular hashtags's information
# for h in top_h:
#     with open(f'{h}.csv', 'w', newline='') as csvfile:
#         fieldnames = ['ID', 'URL', 'Likes', 'Owner', 'Text', 'Date']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
        
#         for post_info in info_dict[h]:
#             writer.writerow({'ID': post_info[0], 'URL': post_info[1], 'Likes': post_info[2], 'Owner': post_info[3], 'Text': post_info[4], 'Date': post_info[5]})
            
# write on count.csv
with open('count.csv', 'w', newline='') as csvfile:
    fieldnames = ['Hashtag', 'Count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for h in count:
        writer.writerow({'Hashtag': h, 'Count': count[h]})