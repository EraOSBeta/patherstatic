import sys
import platform


"""A module consisting of snippets from other modules to minimize the usage of pip,
list of modules used:
 - maskpass"""


class CrossGetch:
    """
    Cross platform getch
    """

    def __init__(self):
        if platform.system() == "Windows":
            import msvcrt
            self.getch = msvcrt.getch
        else:
            self.getch = self.posix_getch

    def posix_getch(self):
        """
        Alternative getch for posix
        Straight from stackoverflow.
        """
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.encode()


def hidech():
    cross_getch = CrossGetch()

    while True:
        char = cross_getch.getch()
        if b"\x03" in char:
            raise KeyboardInterrupt
        elif b"\x1b" in char:
            break
        elif b"\r" in char:
            break
