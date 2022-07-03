import os

from selene import have
from selene.support.shared import browser


def given_opened_registration_form():
    # open url
    browser.open('/automation-practice-form')

    # Delete footer and fixed ban
    browser.execute_script("document.querySelector('#app > footer').style.display='none'")
    browser.execute_script("document.querySelector('#fixedban').style.display='none'")


class student:
    name = 'Dan'
    surname = 'Vu'
    email = 'test@test.ru'
    state = 'NCR'
    city = 'Delhi'


class Gender:
    female = "Female"


class Subjects:
    chemistry = 'Chemistry'
    maths = 'Maths'


def test_submit_form():
    given_opened_registration_form()

    browser.element('#firstName').type(student.name)
    browser.element('#lastName').type(student.surname)
    browser.element('#userEmail').type(student.email)

    gender = browser.element('#genterWrapper')
    gender.all('.custom-radio').element_by(have.exact_text(Gender.female)).click()

    phoneNumberInput = browser.element('#userNumber')
    phoneNumberInput.type('9998887766')

    # Date of Birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('.react-datepicker__year-select').type('2021')
    browser.element("[aria-label='Choose Monday, October 18th, 2021']").click()

    # Subject
    browser.element('#subjectsInput').type(Subjects.chemistry).press_enter()
    browser.element('#subjectsInput').type(Subjects.maths).press_enter()

    browser.element('#hobbiesWrapper').should(have.text('Reading')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../Resources/w9.jpg'))
    browser.element('#currentAddress').type('DC')

    # State and City
    browser.element('#state').click()
    browser.element('#state input').type(student.state).press_enter()
    browser.element('#city input').type(student.city).press_enter()
    browser.element('#submit').click()

    # Checks
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

    browser.elements('table tr').element(1).should(have.text(student.name))
    browser.elements('table tr').element(1).should(have.text(student.surname))
    browser.elements('table tr').element(2).should(have.text(student.email))
    browser.elements('table tr').element(3).should(have.text(Gender.female))
    browser.elements('table tr').element(4).should(have.text('9998887766'))
    browser.elements("table tr").element(5).should(have.text('2021'))
    browser.elements("table tr").element(5).should(have.text('October'))
    browser.elements("table tr").element(5).should(have.text('18'))
    browser.elements("table tr").element(6).should(have.text(Subjects.chemistry))
    browser.elements("table tr").element(6).should(have.text(Subjects.maths))
    browser.elements("table tr").element(7).should(have.text('Reading'))
    browser.elements("table tr").element(8).should(have.text('w9.jpg'))
    browser.elements("table tr").element(9).should(have.text('DC'))
    browser.elements("table tr").element(10).should(have.text(student.state))
    browser.elements("table tr").element(10).should(have.text(student.city))

    browser.element("#closeLargeModal").click()
