#Predicting the demographics of Twitter users from social evidence using website traffic data

In this project, we predict the demographics of Twitter users based on whom they follow. 
Whereas most prior approaches rely on a supervised learning approach, in which individual users are labeled with demographics, we instead create a distantly
labeled dataset by collecting audience measurement data for 1,500 websites (e.g., 50% of visitors to gizmodo.com are estimated to have a bachelor’s degree).
We then fit a regression model to predict these demographics using information about the followers of each website on Twitter.The resulting average heldout
correlation is .77 across six different variables (gender,age, ethnicity, education, income, and child status).
We additionally validate the model on a smaller set of Twitter users labeled individually for ethnicity and gender, finding performance that is surprisingly competitive
with a fully supervised approach.

## Content

This repository is organized as follows: 
* data
* src

###data

* brands.json 		 - 	contains names of 1500 websites
* demo.json   		 - 	contains variables information like gender,age etc for the 1500 websites
* gender.txt  		 - 	accounts used for gender classification
* race.txt    		 - 	account used for race classification
* twitter-cred.json 	 - 	accounts used in data collection

###src

* [data_collection.ipynb]   -	data collection code
* [data_processing.ipynb]   -	data processing code

###Installation

```sh
install [mongodb]
$ pip install anaconda
$ pip install pymongo
$ pip install twython
$ pip install ipython
```

```sh
$ git clone [git-repo-url] aaai-2015-demographics
$ cd aaai-2015-demographics
$ cd src
$ ipython notebook
```

[mongodb]: http://docs.mongodb.org/manual/installation/
[data_collection.ipynb] : http://nbviewer.ipython.org/github/tapilab/aaai-2015-demographics/blob/master/src/data_collection.ipynb
[data_processing.ipynb] : http://nbviewer.ipython.org/github/tapilab/aaai-2015-demographics/blob/master/src/data_processing.ipynb