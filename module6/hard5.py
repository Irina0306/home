from time import sleep
class User:
    def __init__(self, nickname, password, age, hashpass=None):
        self.nickname= nickname
        self.password=hashpass
        self.age=age
    def __str__(self):
        return self.nickname

class Video:
    def __init__(self,title,duration,time_now,adult_mode):
        self.title=title
        self.duration=duration
        self.time_now=0
        self.adult_mode=adult_mode

class UrTube:

    def __init__(self,users,videos,current_users):
        self.users=[]
        self.videos=[]
        self.current_users=None
    def __log_in__(self,login,password):
        hashpass=hash(password)
        for user in self.users:
            if user.nickname == login and user.password ==hashpass:
                self.current_user= user
    def __register__(self,nickname,password,age):
        hashpass =hash(password)
        is_new_user = True
        for  user in self.users:
            if user.nickname==nickname and user.password == hashpass:
               self.current_user = user
               print(f'{nickname} уже существует')
            else:
                new_user = User(nickname,hashpass, age)
                self.users.append(new_user)
                self.current_user= new_user


    def __log_out__(self):
        self.current_users = None

    def __add__(self,*videos):
        for video in videos:
            self.videos.append(video)

    def __get_videos__(self,word):
        lword= word.lower()
        name_videos=[]
        for video in self.videos:
            if video.title.lower().find(lword)!=-1:
                name_videos.append(video.title)
                return name_videos

    def __watch_video(self,title):
        if not self.current_user:
            print('войдите в аккаунт')
            return
        for video in self.videos:
            if video.title=title:
                if video.adult_mode and self.ccurrent_user.age <18:
                    print('доступ запрещен')
                    return
            for time_po in range(video.duration):
                sleep(1)
                video.time_now+=1
                print(video.time_now, end='')
                print('конец')
            video.time_now=0

ur=UrTube()
v1=Video(title:'Лучший язык программирования 2024 года, 288')
v2= Video('Для чего девушкам поень программист,10, adult_mode=True')

ur.add(v1,v2)

print(ur.get_videos('лучший'))
print(ur.__get_videos__('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.watch_video('')




