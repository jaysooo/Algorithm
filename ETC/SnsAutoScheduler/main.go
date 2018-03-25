package main

import (
  "strings"
  "testing"
  "bitbucket.org/tebeka/selenium"
)
func main(){
	TestYahoo()
    
}

func TestYahoo() {
	t *testing.T
    /* We want firefox, don't care about version much */
    caps := selenium.Capabilities {
        "browserName": "firefox",
    }
    wd, _ := selenium.NewRemote(caps, "", "")
    defer wd.Quit()

    /* Navigate to Yahoo */
    wd.Get("http://www.yahoo.com")

    /* Fill the search box */
    input, err := wd.FindElement(selenium.ByName, "p")
    if err != nil {
        t.Error(err.String())
    }
    err = input.SendKeys("golang")
    if err != nil {
        t.Error(err.String())
    }

    /* Hit the search button */
    button, err := wd.FindElement(selenium.ById, "search-submit")
    if err != nil {
        t.Error(err.String())
    }
    err = button.Click()
    if err != nil {
        t.Error(err.String())
    }

    /* See that we get expected result */
    source, err := wd.PageSource()
    if err != nil {
        t.Error(err.String())
    }

    if !strings.Contains(source, "The Go Programming Language") {
        t.Error("Google can't find Go")
    }
}
selenium