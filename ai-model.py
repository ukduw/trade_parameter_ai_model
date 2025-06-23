
# alpha vantage api for market data
    # use last x days from date of data?
# change of plans...
# skip last project, go straight to TA pattern recognition for long-term plays

# TA libraries (TA-Lib, finta, bt...) to script pattern detection
# Create synthetic patterns for pretraining(???)
# Try semi-supervised or active learning to stretch limited labels(?)
# Screen resultant list by fundamentals
    # i.e. region, market cap...
# Then personally check out returned list




#==========#
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