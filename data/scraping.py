from process import hashtag_l2, hashtag_l1, get_hashtag_l2, get_hashtag_l3, hashtag_l3

# first scraped the official nike official account profile page
# retreived 200 posts 
# extract hashtags from those 200 initial posts, as well as the users mentioned in those posts

l1_hashtag, l1_user = hashtag_l1('nike_1.json')
print("number of l1_hashtag: ", len(l1_hashtag)) # 20
print("l1_hashtag: ", l1_hashtag)

# then, find child posts from those 'level-1' hashtags using 'instagram-hashtag-scraper'
# retreived 100 posts from each hashtag
# extract 'level-2' hashtags from those 100 posts, as well as the captions mentioned in those posts
# the level-2 hashtags and the captions are stored in 'nike_full_2.json'

get_hashtag_l2(l1_hashtag, post_per_hashtag=100, output_filename='nike_2.json')

l2_hashtag = hashtag_l2('nike_2.json')
print("number of l2_hashtag: ", len(l2_hashtag)) # 5327
print("l2_hashtag: ", l2_hashtag)

# then, find child posts from those 'level-2' hashtags using 'instagram-hashtag-scraper'
# retreived 10 posts from each hashtag
# extract 'level-3' hashtags from those 10 posts, as well as the captions mentioned in those posts
# the level-3 hashtags and the captions are stored in 'nike_full_3.json'

get_hashtag_l3(l2_hashtag, post_per_hashtag=10, output_filename='nike_3_1.json')

l3_hashtag = hashtag_l3('nike_full_3.json')
print("number of l3_hashtag: ", len(l3_hashtag))
print("l3_hashtag: ", l3_hashtag)



# hashtag_1, hashtag_2, hashtag_3 = l1_hashtag[0], l1_hashtag[1], l1_hashtag[2]

# print(hashtag_1)