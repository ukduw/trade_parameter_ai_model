
# alpha vantage api for market data
    # use last x days from date of data?
# hybrid bot writing dated configs to file
    # how many days worth of personal configs needed?
    # also need to import full screener return vs which ones were added to config...
        # which model needed to learn stock selection? classification?


# model training:
# (necessary to preprocess data?)
    # (handle missing values, remove duplicates, transform data to suitable format for model)
# split data
    # divide data into training (and validation set?) and test sets
    # training data used to train the model
    # (validation set helps tune hyperparameters)
    # test set used to evaluate final performance
# appropriate ai model
    # regression, classification, clustering???
# scikit-learn, TensorFlow, PyTorth...

# iteratively adjust model parameters to minimize a loss function
# monitor training progress
    # track accuracy, precision, recall...
# use validation and test sets to assess trained model's performance, identify flaws
# adjust hyperparameters, refine data...



# Classification for the different setups?
    # use to determine which setups are returned by screener
    # use that to ML which ones from each class are being selected...

# Clustering for trade planning?
    # market data + class + configs = entry/stop
    # don't think Regression is applicable - not trying to use past data to predict anything...
    # ML where to put entry/stop based on price action
    # ML trailing %, position size based on range, risk, etc...