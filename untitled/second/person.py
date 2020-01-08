import  requests


class person:
    total_person=0 #类变量\
    name=''
    sex=""
    province=""
    def __init__(self,name,sex,province):   #实例变量

        print("init the class")
        self.name=name
        self.sex=sex
        self.province=province
        person.total_person+=1
    @classmethod          #类方法，不需要实例对象可以直接调用
    def sex(cls):
        return cls.sex

    @classmethod
    def set_sex(cls,new_sex):
        return new_sex

    @staticmethod   #静态方法
    def set_newname(new_name):

        return "your new name is "+new_name
    def getname(self):
        return self.name

    def age(self,sex):

        self.sex=sex


if __name__=="__main__":
    yang = person("xiao", "female", 'jiangxi')

    print(person.set_sex("hah"))
    print(yang.set_sex("nnn"))
    #print(person.set_newname("dada"))
    # print(yang.set_newname("dda"))
    # print(person.getsex())
    # print(yang.getsex())

    # yang = person("xiao", "female", 'jiangxi')
    #
    # print(yang.getname())
    # print(person.getsex())

    # yang=person("xiao","female",'jiangxi')
    #
    # yang.age("male")
    # print(yang.getsex())
    # print(yang.sex)

