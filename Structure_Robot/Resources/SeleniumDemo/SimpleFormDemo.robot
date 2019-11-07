*** Settings ***
Documentation  Keywords selenium demo
Resource  ../../Locator/Simple_form_demo_Locator.robot

*** Keywords ***
Enter message
    [Arguments]  ${value}
    input text element     ${txt_message}    ${value}

Click show message button
    Click Element Page   ${btn_show_message}

Verify message on page
    [Arguments]  ${message}
    ${the_message}=     get text on page  ${show_message}
    should be equal  ${message}     ${the_message}