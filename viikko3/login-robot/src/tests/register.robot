*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  palle  palle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ap  lituruoho123
    Output Should Contain  Username must contain at least 3 characters (a-z)

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ap!  lituruoho123
    Output Should Contain  Username must contain at least 3 characters (a-z)

Register With Valid Username And Too Short Password
    Input Credentials  aapee  litu
    Output Should Contain  Password must contain at least 8 characters and include at least one non-alphabetic character

# Register With Valid Username And Long Enough Password Containing Only Letters
# # ...

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command