from selene import have
from selene.support.shared import browser


def given_opened_text_box():
    browser.open('/automation-practice-form')
    # Delete footer and fixed ban
    browser.execute_script("document.querySelector('#app > footer').style.display='none'")
    browser.execute_script("document.querySelector('#fixedban').style.display='none'")


def test_submit_form():
    given_opened_text_box()

    # def variables():
    firstname = 'Dan'
    lastname = 'Vu'
    user_email = 'test@test.ru'
    genter_wrapper = 'Female'
    mobile = '89998887766'
    subjects_input = 'Chemistry'
    hobbies_wrapper = 'Reading'
    upload_picture = '/Users/DanVu/PythonProjects/RegistrationForm/Resourses/w9.jpg'
    current_address = 'DC'
    state = 'NCR'
    city = 'Delhi'

    browser.element('#firstName').type(firstname)
    browser.element('#lastName').type(lastname)
    browser.element('#userEmail').type(user_email)
    browser.element('#genterWrapper').should(have.text(genter_wrapper)).click()
    browser.element('#userNumber').type(mobile)
    # Date of Birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('.react-datepicker__year-select').type('2021')
    browser.element("[aria-label='Choose Monday, October 18th, 2021']").click()
    # Sabject
    browser.element('#subjectsInput').type(subjects_input).press_enter()
    browser.element('#hobbiesWrapper').should(have.text(hobbies_wrapper)).click()
    browser.element('#uploadPicture').type(upload_picture)
    browser.element('#currentAddress').type(current_address)
    # State and City
    browser.element('#state').click()
    browser.element('#state input').type(state).press_enter()
    browser.element('#city input').type(city).press_enter()
    browser.element('#submit').click()
    # Checks
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.elements('table tr').element(1).should(have.text(firstname))
    browser.elements('table tr').element(1).should(have.text(lastname))
    browser.elements('table tr').element(2).should(have.text(user_email))
    browser.elements('table tr').element(3).should(have.text(genter_wrapper))
    # browser.elements('table tr').element(4).should(have.text(mobile))
    browser.elements("table tr").element(5).should(have.text('2021'))
    browser.elements("table tr").element(5).should(have.text('October'))
    browser.elements("table tr").element(5).should(have.text('18'))
    browser.elements("table tr").element(6).should(have.text(subjects_input))
    browser.elements("table tr").element(7).should(have.text(hobbies_wrapper))
    browser.elements("table tr").element(8).should(have.text(""))
    browser.elements("table tr").element(9).should(have.text(current_address))
    browser.elements("table tr").element(10).should(have.text(state))
    browser.elements("table tr").element(10).should(have.text(city))
    browser.element("#closeLargeModal").click()
