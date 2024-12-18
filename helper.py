# from urlextract import URLExtract
# import matplotlib as plt
# from wordcloud import WordCloud
# import pandas as pd
# from collections import Counter
# import emoji


# extract = URLExtract()

# def fetch_stats(selected_user,df):

#     if selected_user != "Overall":
#         df = df[df['user']==selected_user]
#     num_messages  = df.shape[0]
#     words=[]
#     for messages in df['message']:
#         words.extend(messages.split())

#     num_media_message = df[df['message'] =='<Media omitted>\n'].shape[0]
#     # num_media_messages = df[df['message'].str.contains('<Media omitted>', na=False)].shape[0]

#     links = []
#     for messages in df['message']:
#         links.extend(extract.find_urls(messages))

#     return num_messages,len(words),num_media_message,len(links)


# def most_busy_user(df):
#     x = df['user'].value_counts().head()
#     df = round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'name','user':'name','count':'percent'})
#     return x,df
    


# def create_wordcloud(selected_user,df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]
    
#     wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
#     df_wc = wc.generate(df['message'].str.cat(sep=" "))
#     return df_wc


# def most_common_words(selected_user,df):
#     # Corrected line using double backslashes
#     f = open('C:\\Users\\rauna\\OneDrive\\miscellaneous\\Desktop\\whatsapp\\stop_hinglish.txt', 'r')

#     stop_words = f.read()
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]
#     temp = df[df['user']!='group_notification']
#     temp[temp['message'] != '<media omitted>\n']
#     words = []
#     for messages in temp['message']:
#         for word in messages.lower().split():
#             if word not in stop_words:
#                 words.append(word)
#     most_common_df = pd.DataFrame(Counter(words).most_common(20))
#     return most_common_df


# def emoji_helper(selected_user,df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]
#     emojis = []
#     for message in df['message']:
#         emojis.extend([c for c in message if c in emoji.EMOJI_DATA])


#     emoji_counts = Counter(emojis).most_common()

#     emoji_df = pd.DataFrame(emoji_counts, columns=['Emoji', 'Frequency'])
#     return emoji_df


















from urlextract import URLExtract
import matplotlib as plt
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji  

extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    num_media_message = df[df['message'] == '<Media omitted>\n'].shape[0]
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_message, len(links)


def most_busy_user(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'index': 'name', 'user': 'percent'})
    return x, df


def create_wordcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc


def most_common_words(selected_user, df):
    # Updated to match the correct path
    with open('C:\\Users\\rauna\\OneDrive\\Desktop\\miscellaneous\\whatsapp\\stop_hinglish.txt', 'r') as f:
        stop_words = f.read()
    
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_counts = Counter(emojis).most_common()
    emoji_df = pd.DataFrame(emoji_counts, columns=['Emoji', 'Frequency'])
    return emoji_df






