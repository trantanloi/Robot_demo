*** Settings ***
Documentation  Keywords common
Library   Selenium2Library
Library   BuiltIn
Resource  ../../Locator/Common_Locator.robot
Resource  ../PHPTravels/PHPTravels.robot

*** Variables ***
${time_out}        10

*** Keywords ***
Open Browser On Page
    [Arguments]    ${url}     ${driver}
    #Create Webdriver    Firefox    my_alias   executable_path=Driver/geckodriver
    open browser   ${url}     ${driver}       executable_path=Driver/geckodriver
    Maximize Browser Window

Clean Up Data
    close browser

Get Title On Page
    [Arguments]  ${txt_title}
    ${title_page}=   get title
    should be equal  ${title_page}  ${txt_title}

Click Search Button
    Click Element   ${btn_search}

Input Keyword
    [Arguments]  ${text_destination}
    wait until element is visible     ${txt_google}
    input text     ${txt_google}    ${text_destination}