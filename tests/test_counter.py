from pages.counter import Counter

def test_counter(browser):
    page = Counter(browser)

    page.open_page()
    page.counter_stormtroopers()
    page.entering_a_number()

    code = page.get_code()
    assert code, "Empty answer"
    print(code)
