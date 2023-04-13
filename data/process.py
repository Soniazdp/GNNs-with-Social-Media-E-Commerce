import json
from apify_client import ApifyClient
import re

def hashtag_l1(output_filename):
    hashtag_from_brand_1 = []
    users_from_brand_1 = []

    # load json file
    with open(output_filename, "r") as f:
        data = json.load(f)

    # get all hashtags from the brand
    for post in data:

        if post['hashtags'] != []:
            for hashtag in post['hashtags']:
                if hashtag not in hashtag_from_brand_1:
                    hashtag_from_brand_1.append(hashtag)

    # get all mentioned users from the brand, and tagged users

        if post['mentions'] != []:
            for user in post['mentions']:
                if user not in users_from_brand_1:
                    users_from_brand_1.append(user)

        # if post['taggedUsers'][0] != None:
        if 'taggedUsers' in post.keys():
            for user in post['taggedUsers']:
                if user['username'] not in users_from_brand_1:
                    users_from_brand_1.append(user['username'])

    # print("Hashtags from brand: ", hashtag_from_brand_1)
    # print("Users from brand: ", users_from_brand_1)
    return hashtag_from_brand_1, users_from_brand_1


def get_child_post(hashtag, limit, output_filename):
    # Initialize the ApifyClient with API token
    client = ApifyClient('apify_api_WCRpvz5mFpWNRtujQQEXadH4niT1gK3qdeLq')
    actor_collection_client = client.actors()
    actor_list = actor_collection_client.list().items

    # pass down the list of hashtags to the actor
    run = client.actor('apify/instagram-hashtag-scraper').call(run_input={
      "hashtags": hashtag,
      "resultsLimit": limit
      # "resultsLimit": limit,
      # 'maxPosts': limit
    })

    dataset_client = client.dataset(run['defaultDatasetId'])
    dataset_items = dataset_client.list_items().items

    # with open(output_filename, 'w') as f:
    #   for item in dataset_items:
    #     f.write(json.dumps(item) + '\n')

    return dataset_items


def get_hashtag_l2(hashtag_list, post_per_hashtag, output_filename):
    # hashtag_list contains l1 hashtags
    # for each hashtag in hashtag_list, get child posts
    with open(output_filename, 'w') as f:
        for i, hashtag in enumerate(hashtag_list):
            out_filename = 'nike_full_2_' + hashtag + str(i) + '.json'
            print('Getting child posts for hashtag: ', hashtag)
            child_hashtag = get_child_post([hashtag], post_per_hashtag, out_filename)
            # child_hashtag is a list containing all the dictionaries for each child post
            # extract hashtags/caption pairs from each child post
            for post in child_hashtag:
                data = {}
                data['l1 hashtag'] = hashtag
                data['id'] = post['id']
                data['caption'] = post['caption']
                data['hashtags'] = post['hashtags']
                data['url'] = post['url']
            
                f.write(json.dumps(data) + '\n')

def hashtag_l2(output_filename):
    l2_hashtag = []

    # load json file
    with open(output_filename, "r") as f:
        for post in f:
            post = json.loads(post)
            if post["hashtags"] != []:
                for hashtag in post["hashtags"]:
                    if hashtag not in l2_hashtag:
                        l2_hashtag.append(hashtag)
    
    # Regular expression pattern to match only English alphabets and digits
    pattern = re.compile(r'^[a-zA-Z0-9]+$')

    # Filter out strings that do not match the pattern
    filtered_list = list(filter(lambda x: pattern.match(x), l2_hashtag))
    return filtered_list


def get_hashtag_l3(hashtag_list, post_per_hashtag, output_filename):
    # hashtag_list contains l1 hashtags
    # for each hashtag in hashtag_list, get child posts
    with open(output_filename, 'w') as f:
        for i, hashtag in enumerate(hashtag_list):
            out_filename = 'nike_full_3_' + hashtag + str(i) + '.json'
            print('Getting child posts for hashtag: ', hashtag)
            child_hashtag = get_child_post([hashtag], post_per_hashtag, out_filename)
            # child_hashtag is a list containing all the dictionaries for each child post
            # extract hashtags/caption pairs from each child post
            for post in child_hashtag:
                data = {}
                data['l1 hashtag'] = hashtag
                data['id'] = post['id']
                data['caption'] = post['caption']
                data['hashtags'] = post['hashtags']
                data['url'] = post['url']
            
                f.write(json.dumps(data) + '\n')

def hashtag_l3(output_filename):
    l3_hashtag = []

    # load json file
    with open(output_filename, "r") as f:
        for post in f:
            post = json.loads(post) # make it into a dictionary
            if post["hashtags"] != []:
                for hashtag in post["hashtags"]:
                    if hashtag not in l3_hashtag:
                        l3_hashtag.append(hashtag)

    # Regular expression pattern to match only English alphabets and digits
    pattern = re.compile(r'^[a-zA-Z0-9]+$')

    # Filter out strings that do not match the pattern
    filtered_list = list(filter(lambda x: pattern.match(x), l3_hashtag))
    return filtered_list

    


