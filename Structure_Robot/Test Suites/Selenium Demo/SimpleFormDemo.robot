*** Settings ***
Documentation  Check Result On Page
Resource   ../../Resources/Common/Common.robot
Variables  ../../Data/SimpleFormDemo.yaml

Test Setup       Open Browser On Page   ${2_1.driver}     ${2_1.url}
Test Teardown    Clean Up Data
Force Tags   Google_Management 1_1

*** Test Cases ***
Test case 1: Single Input Field
    [Documentation]   Input field and verify message
    [Tags]  1_1
    Given get title on page  ${2_1.title}
    When Enter message  ${2_1.value_message}
    And Click show message button
    Then Verify message on page  ${2_1.value_message}