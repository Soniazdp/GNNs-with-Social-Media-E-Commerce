from apify_client import ApifyClient

client = ApifyClient(token='apify_api_A58ZjrGkqjPZCX380ej0DMw6Gcxvzs312RvT')
actor_collection_client = client.actors()
actor_list = actor_collection_client.list().items
print(actor_list)

run = client.actor('apify/instagram-hashtag-scraper').call(run_input={
  "hashtags": [
    "nails"
  ],
  "resultsLimit": 3
})

dataset = client.dataset(run['defaultDatasetId'])

items = dataset.list_items().items

print(items)