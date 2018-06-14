"""
from Hein import nodeutils
reload(nodeutils)
"""


from maya import cmds
from Hein import selectutils


def delete_selected():
    # get selected
    selected = selectutils.list_selected()
    # delete selected
    delete_node(selected)


def delete_node(nodes):
    # delete node
    print('deleting- {}'.format(nodes))
    cmds.delete(nodes)
