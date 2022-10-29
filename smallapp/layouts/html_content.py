from typing import Optional
from smallapp import PACKAGE_ASSETS_DIR, logger
from mako.template import Template

page_tmpl = Template(filename=str(PACKAGE_ASSETS_DIR.joinpath('templates/page.html')))

def html_page(content: str, api_url: Optional[str] = None, css_extra = None):
    try:
        with open(PACKAGE_ASSETS_DIR.joinpath('css/page.css'), 'r') as f:
            css = f.read()
            if api_url is not None:
                css = css.replace("http://localhost:8000", api_url)
    except Exception as e:
        logger.error(f"Can't read page.css: {e}")
        css = ""

    if css_extra:
        css += css_extra

    html = str(page_tmpl.render(content=content,
                                css_head=css,
                                js_head='',
                                js_body='',
                                api_url=api_url))

    return html
