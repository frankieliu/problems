import unittest2
from job_scheduler import job_list as jl

class test_job_list(unittest2.TestCase):

    def setUp(self):
        self.j = jl.job_list(
            done="resources/done.json",
            todo="resources/todo.json",
            updt="resources/updt.json"
        )
        self.j.get_data()
        self.j.update_calc()
        pass

    def test_done(self):
        self.j.get_data()
        self.assertEqual(
            self.j.done,
            {
                12:
                {
                    "id": 12,
                    "data": {
                        "query": "do this",
                        "destination": "a",
                        "time": 1232
                    }
                },
                13:
                {
                    "id": 13,
                    "data": {
                        "query": "do this",
                        "destination": "a",
                        "time": 1232
                    }
                }})

    def test_todo(self):
        self.assertEqual(
            self.j.todo,
            {
                12:
                {
                    "id": 12,
                    "data": {
                        "query": "do this",
                        "destination": "a",
                        "time": 1232
                    }
                },
                13:
                {
                    "id": 13,
                    "data": {
                        "query": "do this",
                        "destination": "a",
                        "time": 1232
                    }
                },
                14:
                {
                    "id": 14,
                    "data": {
                        "query": "do this",
                        "destination": "a",
                        "time": 1232
                    }
                }
            })

    def test_update(self):
        self.assertEqual(
            self.j.updt,
            {
                14:
                {
                    "id": 14,
                    "data": {
                        "query": "do this",
                        "destination": "a",
                        "time": 1232
                    }
                }
            })


if __name__ == "__main__":
    unittest2.main()
