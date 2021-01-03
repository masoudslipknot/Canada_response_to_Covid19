import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

columns = ["Negative_score","Positive_score","Neu_score","Compund_score"]


datasets = ['Raw_March','RawApril','RawAugest','RawJully','RawJune','RawMay','RawOctober','RawSeptember']
sid = SentimentIntensityAnalyzer()
for i in range(0,len(datasets)):
    tweets_score = pd.DataFrame(columns=columns)
    df = pd.read_csv('Raw_datasets_with_three_keywords/'+str(datasets[i]+'.csv'))
    for j in range(0,len(df)):
        current = df.iloc[j]
        current = current.tolist()
        if current[4] and current[5] < 5:
            continue
        else:
            tweet_text = current[2]
            tweet_score = sid.polarity_scores(tweet_text )
            tweets_score = tweets_score.append({"Negative_score": tweet_score['neg'], "Positive_score": tweet_score['pos'],
                                            "Neu_score": tweet_score['neu'], "Compund_score": tweet_score['compound'],
                                                }, ignore_index=True)


    tweets_score.to_csv('Raw_datasets_with_three_keywords/'+str(datasets[i])+'scores.csv')