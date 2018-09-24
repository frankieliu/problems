import inotify.adapters
import importlib
import os.path, time
import sys

class todo:
    """
    Idea:

    - perform an instruction on every change of the 'go' flag
    - 'go' flag serves as a proxy for a message
    - 'todo' defines the payload to run

    Implementation details:

    - payload:
      - resides in a module at the same level as the todo package
        - Note: <module>.main() is run
    - flag:
      - implemented with an inotify on changes to a directory,
        filter only if certain file is touched
    """

    def __init__(self, todo=None, go=None):
        """
        :param todo specifies which module.main() is used
        :param 'go' flag evokes a todo
        """
        self.todo = todo
        if self.todo is not None:
            self.mod = importlib.__import__(self.todo)
        if go is not None:
            self.go = os.path.basename(go)
            self.go_dir = os.path.dirname(go)
        else:
            self.go = None
            self.go_dir = None

    def do(self):
        if self.todo is not None:
            importlib.reload(self.mod)
            self.mod.main()

    def loop(self):

        # always take whatever is present then
        # look for modifications
        self.do()

        # main event loop
        if self.go is not None:
            i = inotify.adapters.Inotify()
            i.add_watch(self.go_dir)
            for event in i.event_gen(yield_nones=False):
                (_, type_names, path, filename) = event
                print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
                    path, filename, type_names))
                if filename == self.go and type_names[0] == 'IN_CLOSE_WRITE':
                    self.do()

def main():
    td = todo(todo="sample_do", go="/tmp/td/go")
    td.loop()

def main2():
    td = todo(todo="sample_query", go="/tmp/td/go")
    td.loop()

if __name__ == "__main__":
    main2()
