'''
Author: Joseph Vanicek
Date: 11/9/2017

Description:
Takes tweets about Donald Trump and Hillary clinton during the last election. It applies sentiment analysis to tweets from from before and after the third presidential debate.
It compares the sentiments between Trump and Clinton to predict the out come of the election based on how people are talking about them
'''




import pandas as pd
import json
from textblob import TextBlob as tb
import numpy as np, matplotlib.pyplot as plt

def get_sentiment(file):
    '''
    Takes a json file of tweets and runs a sentiment analysis on them. 
    Parameters: 
        file: file of tweets
    Returns: the mean and standard deviation of the sentiments polarity.
    '''
    with open(file) as fp:
        data = json.load(fp)
    sent_sub = []
    sent_polar = []
    for x in data:
            tweet = tb(x) 
            tweet_sent = tweet.sentiment
            if tweet_sent.polarity !=0 or tweet_sent.subjectivity !=0:
                sent_polar.append(tweet_sent.polarity)
                sent_sub.append(tweet_sent.subjectivity)
    return [np.mean(sent_polar),np.std(sent_polar,ddof=1)]

def get_ct_sentiment_frame():
    '''
    Creates a data frame of sentiment values for Trump and clinton both before and after the election
    Parameters:none
    Returns: the dataframe
    '''
    t_pre = get_sentiment('trump_tweets_pre.json')
    t_post = get_sentiment('trump_tweets_post.json')
    trump = t_pre+t_post

    c_pre = get_sentiment('clinton_tweets_pre.json')
    c_post = get_sentiment('clinton_tweets_post.json')
    clinton = c_pre+c_post

    index = ['Clinton', 'Trump']
    columns = ['pre_mean', 'pre_std', 'post_mean', 'post_std']
    data = [clinton,trump]
    df = pd.DataFrame(data, index, columns)
    return df

def make_fig(df):
    '''
    create a bar graph with y-error caps to visualize the sentiment data. 
    Parameters:
        df: sentiment frame
    Returns: none
    '''
    data = df[['pre_mean', 'post_mean']].T
    yerr = df[['pre_std','post_std']].T
    data.index = yerr.index = ['Clinton-Trump pre', 'Clinton-Trump post']
    data.columns = yerr.columns = ['Clinton','Trump']
    fig = data.plot.bar(yerr = yerr, legend = True, edgecolor = 'black', color = 'bg',capsize=10)
    ax = plt.gca()
    ax.set_ylabel('Sentiment', color = 'black')
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    
    ax.yaxis.label.set_fontsize(24)
    ax.xaxis.label.set_fontsize(24)
    ax.tick_params(axis='x', colors='black', labelsize=16)
    ax.tick_params(axis='y', colors='black', labelsize=12)
    ax.set_xticklabels( data.index, rotation='horizontal')
    ax.patch.set_facecolor('white')
    plt.gcf().set_facecolor('white')

    

    

    

    
    


    


#==========================================================
def main():
    '''
   Using the above function. This takes the sentiment data and creates the figure.
    '''
    
    make_fig(get_ct_sentiment_frame())

    plt.show()

if __name__ == '__main__':
    main()
