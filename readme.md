# Description
Analyzes the sentiment expressed in tweets containing the keywords 'Clinton' and 'Trump' from before and after the third presidential debate

## Requirements
* **Files**
  * clinton_ tweets_post.json
  * clinton_ tweets_pre.json
  * trump_tweets_post.json
  * trump_tweets_pre.json
* **Python 3 Libraries**
  * Pandas
  * Json
  * Textblob
  * Numpy
  * Matplotlib.pyplot
# Output
![figure](https://github.com/jvanicek/trump-clinton-sentiment/blob/development/sentiment.png)<br>

 
|   |pre_mean   |pre_std   |post_mean   |post_std   |
|---|---|---|---|---|
|Clinton   |-0.000147   |0.260372   |0.057375   |0.381612   |
|Trump   |0.055349   |0.348403   |0.122674   |0.484247   |

**Number of tweets in each file**<br>
trump_tweets_pre.json contains 100 tweets<br>
trump_tweets_post.json contains 100 tweets<br>
clinton_tweets_pre.json contains 82 tweets<br>
clinton_tweets_post.json contains 93 tweets<br>

## Analysis
This sentiment analysis based on tweets before and after the third presidential debate, shows that both candidates increased in positive sentiments after the debate. Clinton started with a slightly negative sentiment of -0.000147 before the debate. Then climbed to 0.057375 post debate, a difference of 0.057522. Trump started out with wit a positive sentiment of 0.055349, then climed to 0.122674, a difference of 0.067325.



