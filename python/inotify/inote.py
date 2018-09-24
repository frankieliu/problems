import inotify.adapters
import os.path, time

def _main():
    i = inotify.adapters.Inotify()

    i.add_watch('/tmp')

    with open('/tmp/test_file', 'w'):
        pass

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        fpath = path+"/"+filename
        print("last modified: %s" % time.ctime(os.path.getmtime(fpath)))
        print("created: %s" % time.ctime(os.path.getctime(fpath)))
        (mode, ino, dev, nlink, uid, gid, size,
         atime, mtime, ctime) = os.stat(fpath)
        print("last modified: %s" % time.ctime(mtime))
        print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
              path, filename, type_names))

if __name__ == '__main__':
    _main()
