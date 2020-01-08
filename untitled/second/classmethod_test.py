class person:
    total_person=0 #类变量
    def __init__(self,name,sex,province):   #实例变量

        print("init the class")
        self.name=name
        self.sex=sex
        self.province=province
        person.total_person+=1
    @classmethod
    def getsex(self):
        return self.sex

    def getname(self):
        return self.name

    def age(self,sex):

        self.sex=sex


if __name__=="__main__":
    yang=person("xiao","female",'jiangxi')

    yang.age("male")
    print(yang.getsex())
    print(yang.sex)

