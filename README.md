# App Lift - Predicting Install Probabilities for ad-bidding.

This was a consulting project during the Insight Data Science fellowship.

The objective here was to present a probabilistic approach for ad bidding by determining which users were most likely to install the app if they were shown an ad.

There are 4 notebooks that denote these steps:

1. Data Extraction
2. Feature Exploration
3. Predictions
4. Probability Model

The data is propietary and can't be shared.

A main challenge to this project was that the classes were imbalanced, 99.5% of the people in the data did not install the app when they saw an ad. To combat this several approaches were used and the one I stuck with is an approach that takes into account the prior conversion rate into account.
