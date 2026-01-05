from abc import ABC

from abc import abstractmethod

class Editor(ABC):

    @abstractmethod
    def create_modules_package(self):
        pass
    @abstractmethod
    def edit(self):
        pass
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def debug(self):
        pass

class vscode(Editor):

    def create_modules_package(self):
        print("vscode can create modules and package")

    def edit(self):
        print("vscode can edit")

    def execute(self):
        print(" vscode can execute")

    def debug(self):
        print("vscode can debug")

vsccode_instance=vscode()

vsccode_instance.create_modules_package()