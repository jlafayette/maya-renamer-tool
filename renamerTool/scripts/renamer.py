import maya.api.OpenMaya as om


def no_empty(arg_index, err_label):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not args[arg_index]:
                om.MGlobal.displayError("No {label} given!".format(label=err_label))
                return
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator


def no_first_digit(arg_index, err_label):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if args[arg_index][0].isdigit():
                om.MGlobal.displayError("{label} cannot begin with a digit!".format(label=err_label.capitalize()))
                return
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator


@no_empty(0, "string to replace")
def replace(old_str, new_str):
    print "Replace '{f}' with '{r}'".format(f=old_str, r=new_str)
    _renamer(_get_replace_func(old_str, new_str))


@no_empty(0, "prefix")
@no_first_digit(0, "prefix")
def add_prefix(prefix):
    print "Add prefix: {p}".format(p=prefix)
    _renamer(_get_prefix_func(prefix))


@no_empty(0, "suffix")
def add_suffix(suffix):
    print "Add suffix: {s}".format(s=suffix)
    _renamer(_get_suffix_func(suffix))


@no_empty(0, "rename string")
@no_first_digit(0, "name")
def rename_and_number(input_str):
    print "Rename and number based on: {i}".format(i=input_str)
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
    om.MGlobal.displayInfo("Renamed {num} objects".format(num=sel.length()))


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
