import os
import sys
projectpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
if projectpath not in sys.path:
    sys.path.append(projectpath)
if curPath not in sys.path:
    sys.path.append(curPath)

from sqlmodel import Session,SQLModel,select
from database.model import Student, Teacher, Quiz, Class, Record,User
from database.database import engine

def add(data:SQLModel):
    """增加数据
    data:要增加的数据对象"""
    with Session(engine) as session:
        try:
            session.add(data)
            session.commit()
            print("add successful")
        except Exception as e:
            session.rollback()
            print(f"Error when adding data:{str(e)}")


def delete_data(data: SQLModel):
    """
    从数据库中删除数据
    :param data: 要删除的数据对象
    """
    # 创建会话
    with Session(engine) as session:
        try:
            # 删除数据
            session.delete(data)
            # 提交会话以将更改写入数据库
            session.commit()
            print("Data deleted successfully!")
        except Exception as e:
            # 如果出现异常，则回滚会话并打印错误消息
            session.rollback()
            print(f"Error deleting data: {str(e)}")

def update_data(data: SQLModel, **kwargs):
    """
    更新数据库中的数据
    :param data: 要更新的数据对象
    :param kwargs: 要更新的属性和值，例如 name="New Name"
    """
    # 创建会话
    with Session(engine) as session:
        try:
            db_data = session.get(type(data), data.id)
            # 更新数据对象的属性
            for attr, value in kwargs.items():
                setattr(db_data, attr, value)
            session.commit()
            print("Data updated successfully!")
        except Exception as e:
            # 如果出现异常，则回滚会话并打印错误消息
            session.rollback()
            print(f"Error updating data: {str(e)}")


def get_data_by_id(model_cls, id):
    """
    通过主键 ID 从数据库中获取数据对象
    :param model_cls: 数据对象的类
    :param id: 要获取的数据对象的主键 ID
    :return: 获取到的数据对象，如果未找到则返回 None
    """
    # 创建会话
    with Session(engine) as session:
        try:
            # 使用主键 ID 查询数据对象
            data = session.get(model_cls, id)
            return data
        except Exception as e:
            print(f"Error getting data: {str(e)}")
            return None



# 注册新用户
def register_student(id,name,class_id,grade=0):
    with Session(engine) as session:
        try:
            class_ = session.query(Class).filter(Class.id == class_id).first()
            if class_ is None:
                session.rollback()
                raise ValueError(f"Class with id {class_id} does not exist")
            else:
                student = Student(id=id,name=name,grade=grade,class_id=class_id)
                add(student)
        except Exception as e:
            session.rollback()
            raise ValueError(f"Error when registering student:{str(e)}")

def register_user(user_id, username, password,class_id,grade=0):
    with Session(engine) as session:
        try:
            user_ = session.query(Student).filter(Student.id == user_id, Student.class_id == class_id).first()

            if user_ is None:

                raise ValueError(f"学生 {user_} 不存在 或者 {user_id} 不在课程 {class_id}\n")
            else:
                user = User(id=user_id, username=username, password=password)
                add(user)
        except Exception as e:
            session.rollback()
            raise ValueError(f"Error when registering：{str(e)}")


def register_teacher(id,name,class_ids:list[int]=None):
    with Session(engine) as session :
        try :
            # 创建教师实例
            new_teacher = Teacher(id=id,name=name)
            if class_ids :
                # 检查每个班级是否存在并建立关联
                for class_id in class_ids :
                    class_ = session.query(Class).filter(Class.id == class_id)
                    if class_ is None :
                        raise ValueError(f"Class with id {class_id} does not exist")
                    else:
                        new_teacher.classes.append(class_)
            # 添加教师到数据库
            session.add(new_teacher)
            session.commit()
            print("Teacher registered successfully")
        except Exception as e:
            session.rollback()
            raise ValueError(f"Error when registering teacher:{str(e)}")


def login_user(user_id: int, password: str) -> User :
    """
    :param user_id: 用户 ID
    :param password: 用户密码
    :return: 如果认证成功，返回 User 对象；否则返回 None
    """
    with Session(engine) as session :
        try:
            user = session.query(User).filter(User.id == user_id)
            if user and user.password == password :
                return user
            else :
                raise Exception("Invalid user ID or password")
        except Exception as e:
            session.rollback()
            raise Exception(f"{str(e)}")


def add_record(r_id,stu_id:int,quiz_id:int,result = "fail"):
    with Session(engine) as session:
        try:
            record =Record(id=r_id,student_id=stu_id,quiz_id=quiz_id,result=result)
            add(record)
        except Exception as e:
            raise ValueError(f"{str(e)}")


if __name__ == '__main__' :
    pass
