from datetime import datetime

def time_checked(func):
    def decorated(*args):
        start_time = datetime.now()
        func(*args)
        end_time = datetime.now()
        print(f'경과시간 {end_time - start_time}')
        print()

    return decorated