import maya.api.OpenMaya as om


def replace(old_str, new_str):
    print "Replace '{f}' with '{r}'".format(f=old_str, r=new_str)
    if not old_str:
        om.MGlobal.displayError("Cannot replace empty string!")
        return
    _renamer(_get_replace_func(old_str, new_str))


def add_prefix(prefix):
    print "Add prefix: {p}".format(p=prefix)
    if _check_empty(prefix, "prefix"):
        return
    if _check_first_digit(prefix, "prefix"):
        return
    _renamer(_get_prefix_func(prefix))


def add_suffix(suffix):
    print "Add suffix: {s}".format(s=suffix)
    if _check_empty(suffix, "suffix"):
        return
    _renamer(_get_suffix_func(suffix))


def rename_and_number(input_str):
    print "Rename and number based on: {i}".format(i=input_str)
    if _check_empty(input_str, "rename string"):
        return
    if _check_first_digit(input_str, "name"):
        return
    _renamer(_get_rename_and_number_func(input_str))


def _renamer(rename_func):
    sel = om.MGlobal.getActiveSelectionList()
    mod = om.MDGModifier()
    for i in range(0, sel.length()):
        dagpath = sel.getDagPath(i)
        mobj = sel.getDependNode(i)
        name = dagpath.fullPathName().split('|')[-1]
        new_name = rename_func(name, count=i)
        mod.renameNode(mobj, new_name)
    mod.doIt()


def _check_empty(input_str, label):
    if not input_str:
        om.MGlobal.displayError("No {label} given!".format(label=label))
        return True
    else:
        return False


def _check_first_digit(input_str, label):
    if input_str[0].isdigit():
        om.MGlobal.displayError("{label} cannot begin with a digit!".format(label=label.capitalize()))
        return True
    else:
        return False


def fix_illegal_name(name_str):
    """Repair names that will cause a RuntimeError

    These include names starting with a number and empty strings.
    Most (maybe all?) other problems will be fixed by converting illegal characters to underscores.

    """
    if not name_str:
        return "_"
    elif name_str[0].isdigit():
        return "_" + name_str
    else:
        return name_str


def _get_replace_func(old_str, new_str):
    def func(name, count):
        new_name = name.replace(old_str, new_str)
        return fix_illegal_name(new_name)
    return func


def _get_prefix_func(prefix):
    def func(name, count):
        return prefix + name
    return func


def _get_suffix_func(suffix):
    def func(name, count):
        return name + suffix
    return func


def _get_rename_and_number_func(input_str):
    def func(name, count):
        """Placeholder function"""
        # TODO: parse input string to find bracket pairs for incrementing
        # TODO: add alphabet incrementing (upper and lower case)
        return input_str + str(count)
    return func
