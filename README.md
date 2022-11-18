<br />
<div align="center">
  <a href='https://postimg.cc/w1KLLpP4' target='_blank'><img src='https://i.postimg.cc/w1KLLpP4/Add-a-subheading.gif' border='0' alt='Add-a-subheading'/></a>
  <h3 align="center">IPFSML</h3>
</div>

## Problem
1. Data scientiest lack on getting different web3 datasets based on there required problem statments.
2. Uploading and retriving machine learning or deep learning models they build was really hard and model management quiet difficult.
3. Need to go differenet data source to grab the required datasets and still hard to search needed data.
4. data and model personalized storage are hard.

## Solutions
1. WEB3 DATA HUB is a common solution, using that people can easliy pull required datasets (easily access via PIP packages)
2. Easy one line cmd to store and pull the models are data as required.
3. Easy one line search cmd to get any data as per requried
4. personalized encrypted data and model storage.


## IPFS

    1. **NFT.storage** and **Web3.storage** are used to store the data
    2. Multiple cron jobs that featch data daily from various platforms
    3. Data cleaning and data validation jobs that clean each datasets before push.
    4. Support encryption if needs.



# Install

    ** pip install IpfsML

## Setup
    
    from IpfsML import store_data_sets

## Get top datasets
    datasets = store_data_sets.get_datasets()

## Search datasets
    search_datasets = store_data_sets.search('Cryptopunks')

## Upload datasets

    upload_datasets = store_data_sets.upload_dataset('chick', 'chicken_nft_.csv')

## Get ML Models

    get_model = store_data_sets.get_model('polygon')

## Upload models

    store_data_sets.upload_model('ETH_model', 'eth.pth')

## Get Popular Models

    store_data_sets.get_models()







    
