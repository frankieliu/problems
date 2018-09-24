import json
import io

class job_list:
    """
    Idea:
    - jobs are entered into a todo list
    - jobs are completed and added to a done list
    - completed jobs are removed from the todo list
      into an updated list
    """
    def __init__(self,done,todo,updt=None):

        self.data = {
            "done": {
                "file": done,
                "data": {}},
            "todo": {
                "file": todo,
                "data": {}},
            "updt": {
                "file": updt,
                "data": {}}
            }

        # shortcuts
        self.done = self.data["done"]["data"]
        self.todo = self.data["todo"]["data"]
        self.updt = self.data["updt"]["data"]
        pass

    def dict_from_json(self, file):
        """
        opens json, array of objects with 'id' child,
        rearranges into dictionary keys by 'id'

        example:

        [{
           "id": 12,
           "data": {
             "query": "do this",
             "destination": "a",
             "time": 1232
           }
         },{ ... }]


        returns:
        {<id0>: {"id": <id0>, "data": {...}},
         <id1>: {"id": <id1>, "data": {...}}, ... }

        """
        return {x["id"]: x for x in
             json.load(open(file))}

    def dict_to_json(self, file, data):
        """
        write to JSON file
        """
        with io.open(file, 'w', encoding='utf8') as outfile:
            str_ = json.dumps(data,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(str(str_))

    def get_data(self):
        """
        updates data dictionary from json files
        """
        for k, v in self.data.items():
            if k != "updt":
                self.data[k]["data"].update(
                    self.dict_from_json(self.data[k]["file"]))

    def update_calc(self):
        """
        performs set operation todo - done
        remove done items from todo list

        result: self.updt contains updated todo list
        """
        # copies todo to updt
        self.updt.update(self.todo)

        # removes done items from updt
        # note: must call list to actually iterate
        if False:
            list(map(self.updt.__delitem__,
                     filter(self.updt.__contains__,
                            self.done.keys())))
        # single pass
        for k in self.done:
            self.updt.pop(k, None)

    def update_write(self):
        updt = self.data["updt"]
        if updt["file"] is not None:
            self.dict_to_json(updt["file"], updt["data"])


def main():
    j = job_list(
        done="done.json",
        todo="todo.json",
        updt="updt.json"
    )
    j.get_data()
    j.update_calc()
    j.update_write()

if __name__ == "__main__":
    main()
