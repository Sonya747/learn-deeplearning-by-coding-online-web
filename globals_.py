"""
global variables:
user_id:用户名
user_identity:"student" or "teacher"
"""
import os
login_: bool = False
user_id:int=100000
user_identity:str="student"
ProjectPath :str= os.path.abspath(os.path.dirname(__file__))
ImagePath:str = ProjectPath + r'/images/'
