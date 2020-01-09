*** Settings ***
#Library   ./testClassFile.py.TestClass    WITH NAME   First_lib

#Resource    Shopping_Search_List.txt

Library   ./EbaySearchFilter.py    ./storage.py    Shopping_Search_List.txt       ${username}      ${password}  ${key}   WITH NAME   First_lib
Library    OperatingSystem
Library     String
Library  Collections
Library  BuiltIn


*** Variables ***
${username}     alex.chandler@utexas.edu
${password}     Twinkie926!
${key}      AlexChan-CelloFin-PRD-640728b69-767c9386
${budget} =  1200

*** Keywords ***


*** Test Cases ***
Show Shopping List
    [Documentation]     Shows shopping list
    ${contents}=    Get file   Shopping_Search_List.txt
    @{lines}=    Split to lines     ${contents}
    :FOR     ${line}     IN     @{lines}
    \   log  ${line}     WARN

LoginTest
    ${responseCode}=    login
    Log     ${responseCode}
    Run Keyword If  '${responseCode}' == '404'  log to console  "could not log in"
    Run Keyword If  '${responseCode}' == '200'  log to console  "Successfully Logged In With Post Command"

BudgetTest
    ${prices} =  get price    get_max=True
    run keyword if  ${prices}<${budget}     log to console  "Within budget"
    run keyword if  ${prices}>=${budget}    log to console  "Outside of budget"


Item Validifier
    [Documentation]     Tests each line to find error
    @{items}=   parse doc
    :FOR     ${item}     IN     @{items}
    \   # ${contains} will be True if "error" is a part of the ${line} value
    \   ${contains}=  Evaluate   "error" in """${item}"""
    \   run keyword if  ${contains}   log to console  "Error finding item"
    \   ...     ELSE    LOG TO CONSOLE  "Valid item"


