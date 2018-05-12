"""
1. conda env list :
   if you see fabric:
    source activate fabric

2. else:
    conda create --name fabric pip
    pip install fabric3

3. running it.
   1. modify my['key_filename'] below
   2. python test_local.py

"""
from __future__ import with_statement
from fabric.api import local, env, run, hide


my = dict()
my['host_string'] = 'sca-t81-133'
my['key_filename'] = '/import/async/cad/2018/m8plus/id_rsa'


def run_sys(cmd):
    env.user = 'root'
    env['host_string'] = my['host_string']
    env.key_filename = my['key_filename']
    with hide('output'):
        return run(cmd)


def run_sp(cmd):
    env.user = 'sunservice'
    env['host_string'] = my['host_string'] + '-sp'
    env.key_filename = my['key_filename']
    with hide('output'):
        return run(cmd)


if __name__ == "__main__":
    local("echo hello")
    print(run_sp("csrdbg /SYS/MB/CM/CMP pmc_dvfs_pstate_table_0 -rv"))
    print(run_sys("/net/melab/export/ld/m8/common/clockrate.py -c 1"))
