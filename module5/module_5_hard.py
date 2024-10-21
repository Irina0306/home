import time

class User:
    def __init__(self,nickname:str,password:int, age:int):
        self.nickname=nickname
        self.password=password
        self.age=age
    def __hash__(self):
        return hash(self.password)

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title=title
        self.duration= duration
        self.time_now=0
        self.adult_mode=adult_mode

class UrTube:
    def __init__(self):
        self.users=[]
        self.videos= []
        self.current_user= None
    def log_in(self,nickname,password):
        for user in self.users:
            if user == user.nickname and password == user.password:
                self.current_user = user
                return

    def log_out(self):
        self.current_user= None

    def register(self, nickname, password, age):
        password= hash(password)
        for user in self.users:
            if nickname in user.nickname:
                print(f'Пользователь {nickname} уже существует')
                #return
                break
        new_user= User(nickname, password, age)
        self.users.append(new_user)
        self.current_user= new_user
        print(f'Вы зарегистрированы')
    def add(self,*files):
        for film in files:
            if film.title not in [video.title for video in self.videos]:
                self.videos.append(film)

    def get_videos(self,text):
        files=[]
        for video in self.videos:
            if text.upper() in video.title.upper():
                files.append(video.title)
        return files

    def watch_video(self,film):
        if self.current_user:
            for video in self.videos:
                if self.current_user and self.current_user.age< 18:
                    print('Вам нет 18, покиньте страницу')
                    return
                if film in video.title:
                    for i in range(1,11):
                        print(i, end=' ')
                        time.sleep(1)
                        video.time_now=0
                        print('Конец')
if __name__=='__main__':
    ur= UrTube()
    v1= Video('Лучший язык программирования 2024 года',200)
    v2= Video('Для чего девушкам парень программист?',10,adult_mode=True)

ur.add(v1,v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin','lolkekcheburek',13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist','iScX4vIJCIb9Q',25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin','F8098FM8fjm',25)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')




