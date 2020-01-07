import random
import string
print(dir(string))
rad_str=''.join(random.choice(string.digits+string.ascii_lowercase+
                      string.ascii_uppercase)for _ in range(8))

print(rad_str+"@163.com")

couerse=["java","python","selenium"]
rande_course=random.choice(couerse)
print(rande_course)

import logging

