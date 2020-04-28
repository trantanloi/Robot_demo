*** Settings ***
Documentation  Keywords php travels
Resource  ../Common/Common.robot
Resource  ../../Locator/PHPTravels_Locator.robot

*** Keywords ***
Login website PHPTravels
    [Arguments]    ${username}      ${password}
    wait element until visible    ${txt_email}      ${time_out}
    input text element   ${txt_email}     ${username}
    wait element until visible    ${txt_password}       ${time_out}
    input text element   ${txt_password}     ${password}
    click element with class name   ${btn_login}
    wait page load  ${menu_admin}     ${time_out}