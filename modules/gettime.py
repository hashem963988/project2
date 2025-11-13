from datetime import datetime

def timenow():
    now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    return (now)


