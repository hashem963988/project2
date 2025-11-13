import os
import psutil
import shutil
from datetime import datetime

from modules.greeting import greeting


user_input = input("your name: ")
greeting(user_input)