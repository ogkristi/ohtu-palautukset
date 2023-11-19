*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Credentials  palle  palle123  palle123
    Submit Credentials  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Credentials  pl  palle123  palle123
    Submit Credentials  Register
    Register Should Fail With Message  
    ...  Username must contain at least 3 characters (a-z)

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Credentials  palle  pallepalle  pallepalle
    Submit Credentials  Register
    Register Should Fail With Message  
    ...  Password must contain at least 8 characters and include at least one non-alphabetic character

Register With Nonmatching Password And Password Confirmation
    Set Credentials  palle  palle123  palle234
    Submit Credentials  Register
    Register Should Fail With Message  Password confirmation failed

Login After Successful Registration
    Set Credentials  palle  palle123  palle123
    Submit Credentials  Register
    Register Should Succeed
    Go To Login Page
    Set Username  palle
    Set Password  palle123
    Submit Credentials  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Credentials  palle  pall3  pall3
    Submit Credentials  Register
    Register Should Fail With Message  
    ...  Password must contain at least 8 characters and include at least one non-alphabetic character
    Go To Login Page
    Set Username  palle
    Set Password  pall3
    Submit Credentials  Login
    Page Should Contain  Invalid username or password

*** Keywords ***
Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Set Credentials
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}