from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QVBoxLayout, QWidget, QAction

from smallapp import SMALLAPP_PACKAGE_DIR, AppData, logger
from smallapp.layouts.html_content import html_page
from smallapp.layouts.reader_web import ReaderWebEnginePage

class ContentWindow(QMainWindow):
    def __init__(self, app_data: AppData, parent=None) -> None:
        super().__init__(parent)
        logger.info("ContentWindow()")

        self._app_data = app_data

        self.setWindowTitle("Content Window")
        self.resize(800, 800)

        self.qwe = self._new_webengine()

        self._ui_setup()
        self._connect_signals()

    def set_qwe_html(self, html: str):
        self.qwe.setHtml(html, baseUrl=QUrl(str(SMALLAPP_PACKAGE_DIR)))

    def render_page_content(self):
        content = """
        <h1>Hello Small App</h1>
        <p>It's a <em>small</em> app.</p>
        """

        html = html_page(content, self._app_data.api_url)

        self.set_qwe_html(html)

    def _ui_setup(self):
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)

        quit_Action = QAction('&Quit', self)
        quit_Action.setShortcut('Ctrl+Q')
        quit_Action.setStatusTip('Quit application')
        quit_Action.triggered.connect(self.close)

        self._menuBar = self.menuBar()
        self._fileMenu = self._menuBar.addMenu('&File')
        self._fileMenu.addAction(quit_Action)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._central_widget.setLayout(self._layout)

        self._layout.addWidget(self.qwe, 100)

        self.render_page_content()

    def _new_webengine(self) -> QWebEngineView:
        qwe = QWebEngineView()
        qwe.setPage(ReaderWebEnginePage(self))

        qwe.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Enable dev tools
        qwe.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        qwe.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        qwe.settings().setAttribute(QWebEngineSettings.WebAttribute.ErrorPageEnabled, True)
        qwe.settings().setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)

        return qwe

    def _connect_signals(self):
        pass
