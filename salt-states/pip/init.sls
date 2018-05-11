
# pip cannot be found by salt-stack
# the one installed by salt-stack is not working properly
# maybe it can be used later on

#python-pip:
#  pkg.installed
#
#pip requirements:
#  pip.installed:
#    - name: 'Flask'

# using cmd as a workaround for the mentioned bug
pip requirements:
  cmd.run:
    - name: 'pip install --trusted-host pypi.python.org -r pip/files/requirements.txt'
    - cwd: /app/salt-states
