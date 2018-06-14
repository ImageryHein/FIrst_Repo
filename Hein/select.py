"""
from Hein import select
reload(select)
"""
from maya import cmds


def list_selected():
    selection = cmds.ls(selection=True)
    print(selection)
    return selection

