import sys
import traceback
import threading

from PyQt5.QtWidgets import QApplication

from smallapp import AppData, logger
from smallapp.layouts.content_window import ContentWindow
from .api import start_server, find_available_port
from .layouts.error_message import ErrorMessageWindow


def excepthook(exc_type, exc_value, exc_tb):
    logger.error("excepthook()")
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    logger.error(tb)
    w = ErrorMessageWindow(user_message=None, debug_info=tb)
    w.show()


sys.excepthook = excepthook


def start():
    logger.info("start()", start_new=True)

    app = QApplication(sys.argv)

    try:
        port = find_available_port()
        logger.info(f"Available port: {port}")
        daemon = threading.Thread(name='daemon_server',
                                target=start_server,
                                args=(port,))
        daemon.setDaemon(True)
        daemon.start()
    except Exception as e:
        logger.error(e)
        # FIXME show error to user
        port = 6789

    app_data = AppData(api_port=port)

    # === Create first window ===

    view = ContentWindow(app_data=app_data)
    view.show()

    status = app.exec()

    logger.info(f"start() Exiting with status {status}.")
    sys.exit(status)
