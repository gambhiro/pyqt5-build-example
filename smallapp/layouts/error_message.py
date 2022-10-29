import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTextBrowser,
                             QPushButton, QLabel, QMainWindow, QSizePolicy)


class ErrorMessageWindow(QMainWindow):
    def __init__(self, user_message=None, debug_info=None, status=None) -> None:
        super().__init__()
        self.setWindowTitle("Application Error")
        self.setFixedSize(800, 800)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        self._layout = QVBoxLayout()
        self._central_widget.setLayout(self._layout)

        self._msg = QLabel()
        self._msg.setWordWrap(True)

        if user_message:
            self._msg.setText(user_message)
        else:
            self._msg.setText("<p>The application encountered and error.</p>")

        self._msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._layout.addWidget(self._msg)

        if debug_info:
            debug_info = f"```\n{debug_info}\n```"

            self._debug_info = QTextBrowser()
            self._debug_info.setText(debug_info)
            self._debug_info.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

            self._layout.addWidget(self._debug_info)

        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 20, 0, 10)

        self._continue_button = QPushButton("Continue")
        self._continue_button.setFixedSize(100, 30)
        self._quit_button = QPushButton("Quit")
        self._quit_button.setFixedSize(100, 30)

        self._continue_button.clicked.connect(partial(self.close))
        self._quit_button.clicked.connect(partial(self._close_and_quit))

        buttons_layout.addWidget(self._continue_button)
        buttons_layout.addWidget(self._quit_button)

        self._layout.addLayout(buttons_layout)

    def _close_and_quit(self):
        self.close()
        status = 1
        logger.error(f"Exiting with status {status}.")
        sys.exit(status)
