from datetime import datetime

def time_checked(func):
    def decorated():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        print(f'경과시간 {end_time - start_time}')

    return decorated