"""Main module of valessiobrito/uitest Kytos Network Application.

UI Test NApps
"""

from kytos.core import KytosNApp, log

from napps.valessiobrito.uitest import settings


class Main(KytosNApp):
    """Main class of valessiobrito/uitest NApp.

    This class is the entry point for this napp.
    """

    def setup(self):
        """Replace the '__init__' method for the KytosNApp subclass.

        The setup method is automatically called by the controller when your
        application is loaded.

        So, if you have any setup routine, insert it here.
        """
        log.info("Hello world! Now, I'm loaded!")

    def execute(self):
        """This method is executed right after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        log.info("Hello world! Now, I'm executed!")

    def shutdown(self):
        """This method is executed when your napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        log.info("Bye Bye!")
