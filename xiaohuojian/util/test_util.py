import yaml

class TestYaml(object):
    def test_yaml(self):
        dict=yaml.load(open("../data/mainpage.yaml","r"))
        print(dict)
        for value in dict.values():
            for step in value:
                print(step['by'])
                print(step['locator'])
