*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Front Page Opens
    Go To  ${HOME_URL}
    Get Text  h2  ==  Miniprojekti app

Add A Book
    Go To  ${HOME_URL}
    Fill Text  input[name="author"]  Robert
    Fill Text  input[name="editor"]  Prentice Hall
    Fill Text  input[name="title"]  Clean Code
    Fill Text  input[name="publisher"]  Pearson
    Fill Text  input[name="year"] >> nth=0  2008
    Fill Text  input[name="year"] >> nth=1  2008
    Fill Text  input[name="volume"]  1
    Fill Text  input[name="number"]  1
    Fill Text  input[name="pages"]  464
    Fill Text  input[name="month"]  August
    Fill Text  input[name="note"]  Classic
    Fill Text  input[name="doi"]  10.1000/clean
    Fill Text  input[name="issn"]  1234-5678
    Fill Text  input[name="isbn"]  978-0132350884
    Click  text=Add a reference
    Get Text  body  contains  Clean Code