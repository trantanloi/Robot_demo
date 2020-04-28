*** Settings ***
Documentation  Test login function website
Resource   ../../Resources/Common/Common.robot
Variables  ../../Data/PHPTravels.yaml

Test Setup      Open Browser On Page   ${1_1.url}    ${1_1.driver}
Test Teardown   Clean Up Data
Force Tags   Google_Management 1_1

*** Test Cases ***
Test Case 01: Login successfully
    [Documentation]  Test Result About Title
    [Tags]  1_1_2
    Given get title on page  ${1_1.title}
    When Login website PHPTravels   ${1_1.username}     ${1_1.password}
    Then get title on page   ${1_1.title_admin}