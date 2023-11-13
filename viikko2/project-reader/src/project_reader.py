import tomllib
from urllib import request
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        project = tomllib.loads(content)['tool']['poetry']
        name = project['name']
        descr = project['description']
        license = project['license']
        authors = project['authors']
        dep = project['dependencies'].keys()
        devdep = project['group']['dev']['dependencies'].keys()

        return Project(name, descr, license, authors, dep, devdep)
