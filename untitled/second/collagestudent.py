from second.person import person
from second.student import student

class collagestudent(student):
    def __init__(self,name,sex,province,grade):
        student.__init__(self,name,sex,province,grade)
    def has_peer(self):
        pass



if __name__=="__main__":
    da=collagestudent('name', 'sex', 'province', 'grade')
    da.has_peer()
