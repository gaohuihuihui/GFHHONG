import pytest
import random
@pytest.mark.parametrize("x",[
    (3),
    (5)
])

def test_add3(x):
    assert x==random.randrange(1,7)
    # print(random.randint())


@pytest.mark.parametrize("usr_name,password"
                         ["dev","codemao123456"],
                         ["gaofeihong","codemao123456"],
                         ["gaofeihong","codemaogao123"]
                          )
def test_login(usr_name,password):
    assert id(usr_name)==id(password)



def test_add4():
    pytest.assume(1==2)
    pytest.assume(1==1)