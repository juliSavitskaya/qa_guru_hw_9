from pages.registration_page import RegistrationPage
from users.user import student


def test_registration_form(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open().register(student).should_have_registered(student)