# Canada_response_to_Covid19
In this project, I focus on collecting tweets from March until now to see people's opinions toward Canada's management of Covid19. <br>
At first, we collect tweets for each month separately with the following keywords: "Canada", "Management", "Covid". Also, we save different information about each account that tweeted such as follower counts, friends counts, when the account was created, etc. <br>
The reason for saving this extra information is to ignore tweets from fake accounts who were created just before the tweet with 0 follower counts to provide fair results based on people's opinions toward Canada management during the whole period in each month. <br>
<hr>
In the second method of the code, we first ignore the fake accounts and fake tweets. Then, we use pre-trained NLP models to perform a sentimental analysis on tweets to find how positive or negative each tweet is. After doing so, we average the whole positive and negative scores to find out the overall opinion in each month.
<hr>
Finally, we compare people responses in different months from March until now to see how people think toward Canada management regarding Covid19.<br>
<hr>

In Raw_datasets_with_three_keywords, you can find tweets for just march with these three keywords which contains: "Canada", "management", and "Covid19". As a result, the number of tweets is few. This means that few people who were expressing their opinions toward management used the management keyword. We will perform the sentimental analysis on these tweets as well.</br>
However, we will focus on two keywords, namely "Canada" and "Covid19" to make sure all tweets are included. We will use pre-trained NLP models to first classify the topic of each tweet and consider those tweets that their topics are close to management. Then, we will follow the sentimental process for these tweets as well.
<hr>

STILL WORKING ON THE PROJECT!


Writer: <br>
Masoud Erfani


