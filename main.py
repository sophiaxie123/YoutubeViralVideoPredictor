import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret_615288565318-dd7us4i9infmai01fr3n2nlff2cb44f3.apps.googleusercontent.com.json"

flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)


# uses the youtube api to search for the first 25 videos of the given keyword
# returns the ids of these videos
def simple_search(keywords, num_results):
    request = youtube.search().list(
        q=keywords,
        part="id",
        type="video",
        fields="items/id",
        maxResults=num_results)

    response = request.execute()

    videos = []
    for search_result in response.get("items", []):
        videos.append("%s" % (search_result["id"]["videoId"]))

    return videos


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    music_vids = simple_search("music", 2)
    sports_vids = simple_search("sports", 2)
    gaming_vids = simple_search("gaming", 2)
    movies_vids = simple_search("movies and shows", 2)
    news_vids = simple_search("news", 2)
    live_vids = simple_search("live", 2)
    fashion_vids = simple_search("fashion and beauty", 2)
    learning_vids = simple_search("learning", 2)

    print(music_vids)
    print(sports_vids)
    print(gaming_vids)
    print(movies_vids)
    print(news_vids)
    print(live_vids)
    print(fashion_vids)
    print(learning_vids)

    df = pd.DataFrame(
        data=music_vids + sports_vids + gaming_vids + movies_vids + news_vids + live_vids + fashion_vids + learning_vids,
        columns=["Video_IDs"])
    print(df)

    df.to_csv('video_ids.csv', index=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
