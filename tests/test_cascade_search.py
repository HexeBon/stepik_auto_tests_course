from pages.cascade_search import Cascade

def test_cascade_search(browser):
    page = Cascade(browser)

    page.open()
    page.find_parent_element()
    page.find_child_element()

    password = page.get_password()
    assert password, "Empty password"
    print(password)

