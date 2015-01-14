This repository contains data and code to reproduce the results of the paper "[Predicting the demographics of Twitter users from website traffic data](http://www.cs.iit.edu/~culotta/pubs/culotta15predicting.pdf)", by Aron Culotta, Nirmal Ravi, and Jennifer Cutler, presented at the 29th AAAI Conference on Artificial Intelligence ([AAAI-15](http://www.aaai.org/Conferences/AAAI/aaai15.php)), 2015.

## Abstract

Understanding the demographics of users of online social networks has important applications for health, marketing, and public messaging. In this paper, we predict the demographics of Twitter users based on whom they follow. Whereas most prior approaches rely on a supervised learning approach, in which individual users are labeled with demographics, we instead create a distantly labeled dataset by collecting audience measurement data for 1,500 websites (e.g., 50% of visitors to gizmodo.com are estimated to have a bachelor's degree). We then fit a regression model to predict these demographics using information about the followers of each website on Twitter. The resulting average held-out correlation is .77 across six different variables (gender, age, ethnicity, education, income, and child status). We additionally validate the model on a smaller set of Twitter users labeled individually for ethnicity and gender, finding performance that is surprisingly competitive with a fully supervised approach.

## Content

This repository is organized as follows: 
* [`data`](data/): (some) of the data used in the experiments.
* [`src`](src/): iPython notebooks to reproduce results.

###[`data`](data/)

* `brands.json` : contains names of 1500 websites
* `demo.json`   : contains variables information like gender,age etc for the 1500 websites
* `twitter-cred.json` : accounts used in data collection

###[`src`](src/)

* `data_collection.ipynb` : data collection code
* `data_processing.ipynb` : data processing code

###Installation and configuration

1. [Install MongoDB](http://docs.mongodb.org/manual/installation/)
2. Install python modules
```sh
$ pip install anaconda
$ pip install pymongo
$ pip install twython
$ pip install ipython
$ pip install twutil
```
3. Add your twitter credentials to [`data/twitter-cred.json`](data/twitter-cred.json).
4. Clone this repo
```sh
$ git clone https://github.com/tapilab/aaai-2015-demographics.git
```
5. Run the notebooks
```sh
$ cd aaai-2015-demographics/src
$ ipython notebook --matplotlib inline data_collection.ipynb
$ ipython notebook --matplotlib inline data_processing.ipynb
```

### Static Notebooks

Static versions of the iPython notebooks are here:

- [data_collection.ipynb](http://nbviewer.ipython.org/github/tapilab/aaai-2015-demographics/blob/master/src/data_collection.ipynb)
- [data_processing.ipynb](http://nbviewer.ipython.org/github/tapilab/aaai-2015-demographics/blob/master/src/data_processing.ipynb)
