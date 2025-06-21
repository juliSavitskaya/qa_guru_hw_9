import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(driver):
    try:
        logs = driver.get_log('browser')
        log_text = "\n".join(str(log) for log in logs)
    except Exception as e:
        log_text = f"Логи недоступны: {e}"
    allure.attach(log_text, 'browser_logs', AttachmentType.TEXT)


def add_html(browser):
    html = browser.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.session_id, AttachmentType.HTML, '.html')
