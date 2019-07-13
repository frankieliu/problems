sites = '''1-getting-started.txt
best_practices.txt
classes.txt
datastructures.txt
dbapi.txt
functional-programming.txt
functional_programming.txt
getting-started.txt
index.txt
iterators.txt
modules.txt
object_oriented_programming.txt
references.txt
standard_library.txt
sudoku.txt
threads.txt
varargs.txt
working-with-data.txt
'''
import subprocess
outdir = './book/'
base = 'https://anandology.com/python-practice-book/_sources'
for x in sites.splitlines():
    subprocess.run(
        "wget {}/{} -P {}".format(base, x, outdir),
        shell=True)
