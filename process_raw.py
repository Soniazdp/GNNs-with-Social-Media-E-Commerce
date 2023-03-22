import json
from test import get_dataset

def process_raw(hashtag_list):
    # load json file
    with open('output.json', "r") as f:
        data = json.load(f)
    
    # parse it to get the dictionary
    dic = {h:[] for h in hashtag_list}

    for post in data:
        for hashtag in hashtag_list:
            if hashtag in post['hashtags'] and len(dic[hashtag]) < 10:
                dic[hashtag].append(post['ownerId'])
                
    # check if the number of posts is correct
    incomp_hashtag = []
    for hashtag, ids in dic.items():
        if len(ids) < 10:
            print(f"{hashtag} has {len(ids)} elements")
            incomp_hashtag.append(hashtag)
    
    # # if incomplete hashtags exist, get additional data for them
    # while incomp_hashtag:
    #     hashtag = incomp_hashtag.pop()
    #     print(f"Getting additional data for {hashtag}")
    #     additional_data = get_dataset([hashtag], limit=10-len(dic[hashtag]))
    #     for item in additional_data:
    #         if item['ownerId'] not in dic[hashtag]:
    #             dic[hashtag].append(item['ownerId'])
        
    #     # check again if the number of posts is correct for this hashtag
    #     if len(dic[hashtag]) < 10:
    #         print(f"Still missing posts for {hashtag}")
    #         incomp_hashtag.append(hashtag)

    return dic
    
    
if __name__ == "__main__":
    h_list = ['fentybeauty', 'sephora', 'hudabeauty', 'maccosmetics', 'narscosmetics', 'bobbibrown', 'diormakeup','charlottetilbury','makeupforever','anastasiabeverlyhills','urbandecay','tartecosmetics','katvondbeauty','benefitcosmetics','toofaced','morphebrushes','maybelline','nyxcosmetics','revlon','lauramercier','laneige','lancome','clinique', 'esteelauder', 'colourpop'] 
    dict1 = process_raw(h_list)
    
