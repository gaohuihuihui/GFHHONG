
#这是一个继承父类的案例：


from second.person import person
class student(person):
    def __init__(self,name,sex,province,grade):
        print("init student class")
        person.__init__(self,name,sex,province)
        self.grade=grade

    def get_grade(self):
        return self.grade


if __name__=="__main__":
    xiao=student("xiao","male","guangdong","he")
    print(dir(xiao))



    print(xiao.grade)