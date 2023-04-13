# HybridRecommender

Social media has become an increasingly essential tool for e-commerce brands, where they can understand relationships between different products, develop products catering to new trends, and eventually gain a competitive advantage in the market. Traditionally, companies rely on the experience and intuition of industrial analysts or influencers for trend prediction. While these methods may be effective, their performance in trend identification is poorer than data-driven methods using statistical models or machine learning.

This project aims to take full advantage of social media posts about products, from both com- panies and users, to analyze potential connections between hashtags using Graph Neural Network (GNN), in which way to predict future product and social media trend.

## Usage
### Data Acquisition & Processing with Python
Using `data/process.py` and `data/scraping.py`, the ApifyClient API can be accessed with a proper token where a specific number of posts with the desired hashtag will be scraped. Note that due to the limitation of free trials, some manual work on data balancing may be needed. That is, if there are hashtags with not enough posts scraped which can be checked by `process.py`, they need to be fed to the API again such that all hashtags have the same amount of information acquired. Sample hashtags scraped from nike and mac are stored in the json file, which contains 3 levels of hashtag branching out from the brand account.

Then, `data/json_csv.py` should be applied to clean up post information and export the level 3 hashtags for later use. The outputs from this script are ready to pass down to the R scripts.

### Graph Creation with R
`data/hashExtractor.R` scans through all the post texts and extracts related hashtags by tokenizing them. It also captures the frequency of each hashtag for later usage and organizes the hashtags with their frequency in .csv format. Note that hashtags with degree lower than 80 are filtered out for the purpose of data cleaning. Then, Stage 1 of the entire process is finished.

`data/graphCreator.R` reads from the .csv file generated from the previous script and generates an edge matrix. Then it calculates the degree of each hashtag (i.e number of connections to other hashtags). To improve the link prediction of the hashtags that have a lower frequency, the ones with a lower degree will be more focused.

### Model Training
The Graph Neural Network (GNN) model can be found in the `code/exp_gnn.ipynb` script with 2 ConvSage layer and 30 training epochs. 

## Acknowledgement
The R scripts are provided by the open-source GitHub repository: https://github.com/JonasSchroeder/InstaCrawlR

The GNN model is built based on the tutorial provided in the link: https://docs.dgl.ai/en/0.8.x/tutorials/blitz/4_link_predict.html
