import sys

try:
    import PySide6
except ImportError:
    PySide6 = None


def open_folder_picker():
    """
    Opens a folder picker dialog and returns the selected folder path.

    Returns:
        str: The path of the selected folder.
    """

    if PySide6 is not None:
        from .bases.qt import QtFolderPicker

        picker = QtFolderPicker()
    else:
        match sys.platform:
            case "win32":
                from .bases import WindowsFolderPicker

                picker = WindowsFolderPicker()
            case "darwin":
                from .bases import MacOSFolderPicker

                picker = MacOSFolderPicker()
            case "linux":
                from .bases import LinuxFolderPicker

                picker = LinuxFolderPicker()
            case _:
                raise NotImplementedError(f"Unsupported platform: {sys.platform}")

    return picker.pick_folder()
