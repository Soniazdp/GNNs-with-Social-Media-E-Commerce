from apify_client import ApifyClient

def get_dataset(hashtag_list, limit=10, output_filename='output.json'):
    # Initialize the ApifyClient with API token
    client = ApifyClient('our_token')
    actor_collection_client = client.actors()
    actor_list = actor_collection_client.list().items

    # pass down the list of hashtags to the actor
    run = client.actor('apify/instagram-hashtag-scraper').call(run_input={
      "hashtags": hashtag_list,
      "resultsLimit": limit,
    })

    dataset = client.dataset(run['defaultDatasetId'])
    dataset.download_items(limit=limit, format='json')
