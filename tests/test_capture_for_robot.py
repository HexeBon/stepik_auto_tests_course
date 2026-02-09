from pages.capture_for_robot import CaptureForRobot


def test_select(browser):
    page = CaptureForRobot(browser)

    page.open_page()
    page.select()
    page.click_submit()

    text = page.accept_alert()
    assert "28" in text, "NO"
    print(text)