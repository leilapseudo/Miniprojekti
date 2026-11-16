*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Front Page Opens
    Go To  ${HOME_URL}
    Get Text  h2  ==  Miniprojekti app
