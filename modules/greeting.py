from .gettime import timenow

def greeting(user_input):
    now = timenow()
    print (f"{now} Hi {user_input}")
