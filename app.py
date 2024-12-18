import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
from wordcloud import wordcloud

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("upload a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)
    user_list = df['user'].unique().tolist()
    st.sidebar.selectbox("Show analysis wrt",user_list)

    # user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")


    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):

        # Stats Area
        num_messages, words, num_media_messages, num_links= helper.fetch_stats(selected_user,df)
        # st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total words")
            st.title(words)

        with col3:
            st.header("media shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links shared")
            st.title(num_links)

        if selected_user == "Overall":
            st.title("most busy users")
            x, new_df= helper.most_busy_user(df)
            fig, ax =  plt.subplots()
            col1,col2= st.columns(2)
            with col1:
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        df_wc = helper.create_wordcloud(selected_user,df)
        fig ,ax = plt.subplots()

        ax.imshow(df_wc)
        st.pyplot(fig)



        most_common_df = helper.most_common_words(selected_user,df)

        fig,ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation = 'vertical')
        st.title("most common words")
        st.pyplot(fig)
        # st.dataframe(most_common_df)

        st.title("emoji analysis")
        emoji_df = helper.emoji_helper(selected_user,df)

        col1, col2 =st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax = plt.subplots()
            ax.pie(emoji_df['Frequency'].head(), labels=emoji_df['Emoji'].head(), autopct='%.2f', startangle=90)
            st.pyplot(fig)
        # st.dataframe(emoji_df)








































