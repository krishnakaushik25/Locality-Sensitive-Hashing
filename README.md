# Locality Sensitive Hashing Python Code for Look-Alike Modelling

This project idea is based on the research paper below: [A Sub-linear, Massive-scale Look-alike Audience Extension System](http://proceedings.mlr.press/v53/ma16.pdf)
## Business Objective

Let’s say you wish to generate brand awareness of your product and increase its sale; online advertising is the easiest way to do it. Online advertising is considered one of the most effective and efficient ways for businesses of all sizes to expand their reach, find new customers, and diversify their revenue streams.

 

Online advertising is the art of using the internet as a powerful platform to deliver marketing messages to an intended audience. Social media is one the most popular online pastimes for people worldwide, and advertisers have evolved their strategies to target consumers on social media sites like Facebook, Instagram, Twitter, etc. It helps in attracting website traffic and brand exposure, which in turn helps in increasing sales. Hence, online adverting is designed in such a way as to persuade the targeted customer to make a purchase. 

 

But, when these ads get advertised, not all people will be interested in the product/service, and only those interested click on the ads. Click rate is a term that helps us find the percentage of people who have watched your ad online and have ended up clicking it. Hence the goal of online advertising is to reach maximum and relevant users. 

 

So, to find these relevant users/customers, we make use of the Lookalike model. 

Lookalike models are models used to build larger audiences from smaller segments to create reach for advertisers. The more significant users reflect the benchmark characteristics of the original users, which are known as the seed users. 

 

In this project, we will build a Lookalike model that will help us find similar and relevant customers with the help of the LSH – Locality Sensitive Handling algorithm. This algorithm will hence improve the click rate.

 

 

## Data Description 


The dataset used is from a company called ‘Adform’. This dataset is from a particular online digital online campaign. This ad was shown to several thousand people and recorded whether the people clicked the ad or not. As the dataset is vast, only a subset of the dataset was considered. Following is the description of the data:

 

The file is unzipped and each line corresponds to a single record, serialized as JSON. The JSON has the following fields:

- "l": The binary label indicating whether the ad was clicked (1) or not (0).

- "c0" - "c9": Categorical features which were hashed into a 32-bit integer.

- Here, c6 and c9 have multiple values per user and the rest have single value per user.

To know more about the dataset, access the following link:

https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/TADBY7

 

## Aim


To build a lookalike model to find similar users using the Locality Sensitive Hashing algorithm and find an increase in click rate w.r.t the default click rate.


## Tech stack 

Language - Python

Libraries - scikit-learn, pandas, numpy, pickle, yaml, datasketch 

 

## Approach 

1.Importing the required libraries and packages

2.Open the config.yaml file. (This is a configuration file that can be edited according to your dataset)

3.Read the JSON file

4.Clean the JSON file

    - Reset index in the data
    
    - Convert list to integers
    
    - Remove rows above certain threshold values
    
    - Replace empty values with an empty list if any
    
    - Store the cleaned file
    
    - Calculate feature counts for scoring
    
5.Model Training

    - Create a MinHashForest Model
    
    - Create an LSH graph object
    
    - Train the model
    
    - Save the model to a pickle file
    
6.Seed set Extension

    - Read the saved model
    
    - Read the seed set data
    
    - Retrieve the neighbors of seed set from LSH graph
    
    - Calculate the default click rate
    
    - Score the neighbors
    
    - Create and store the extension file
    
    - Find the increased click rate.
