"""
from Hein import selectutils
reload(selectutils)
"""
from maya import cmds


def list_selected():
    selection = cmds.ls(selection=True)
    return selection

