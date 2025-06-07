from pymongo import MongoClient

client = MongoClient("mongodb+srv://Dhurwey2002:Dhurwey2002@cluster0.8yezogk.mongodb.net/", tlsAllowInvalidCertificates= True)
# NOt a good idea to include id and password in code files
# tlsAllowInvalidCertificates= True -> not a good idea to handle

db = client["video_manager"]
video_collection =db["videos"]

print(video_collection)

def add_video(name,time):
    video_collection.insert_one({"name": name, "time":time})

def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']},and Time: {video['time']}")



def update_video(video_id,new_name,new_time):
    video_collection.update_one(
        {'_id':video_id},
        {"$set":{"name": new_name, "time":new_time} }
    )

def delete_video(video_id):
    video_collection.delete_one({"_id":video_id})


def main():
    while True:
        print("\n video manager App")
        print("1. List all videos: ")
        print("2. Add a new video: ")
        print("3. update a video: ")
        print("4. Delete a video: ")
        print("5. Exit App: ")
        choice= input("Enter your choice: ")

        if choice=='1':

            list_all_videos()
        elif choice == '2':
            name= input("Enter the video name: ")
            time = input("Enter the  video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter the videon id to be updated: ")
            name= input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            
             video_id = input("Enter the videon id to be deleted: ")
             delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invailid choice")



        




if __name__=="__main__":
    main()