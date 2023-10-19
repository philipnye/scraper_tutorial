# Purpose
A Python exercise, designed to introduce you to web-scraping. In this case, you'll be scraping the Ofsted ratings of free schools.

Note: These instructions are designed for Windows machines. Steps may vary on other operating systems.

# Prerequisites
- [Visual Studio Code](https://code.visualstudio.com/download) with the following extensions installed:
  - TODO: Complete
- [Python 3.9+](https://www.python.org/downloads/)
  - I'd suggest using all of the default install options bar one: tick the box to add Python to PATH

<img src="img\add_python_to_path.png" alt="Python install step showing how to add Python to PATH" width="500"/>

# Steps
1. Open Visual Studio Code and start a new file (`Ctrl + N`). Save the file - create a new folder called `Free school Ofsted ratings scraper`, and save the file inside, naming it `scraper.py`.

1. At the top of your script type `# %%`. This creates an interactive cell - that is, something you'll be able to run, with the output displayed alongside.

1. Write `print('Hello world')` on the second line and click the `Run Cell` button at the top of the cell. In the output window that appears you'll know that your script has run successfully because there'll be a green tick, and the message `Hello world` will appear.

1. Next, you'll need to install a package called Beautiful Soup that you'll need as part of your scraper. To do this, press `Ctrl + Shift + P` to open Visual Studio Code's Command Palette and start typing "terminal" in the box that appears. An option named `Python: Create Terminal` should pop up - run that command, either by clicking on it, or hitting `Return` when it's highlighted.

1. In the terminal that pops up, type `pip install beautifulsoup4` to start the installation. (Note: This is dependent on you having added Python to PATH, as mentioned above.)

1. You'll also need a package called `requests`, which will allow you to make HTTP (web) requests. Once Beautiful Soup has finished installing, type `pip install requests` in the terminal. Once that's installed you can close the terminal by clicking the X at the top-right of the terminal window.

1. Next, take a look at a sample free school page on the Ofsted website - in a browser go to https://reports.ofsted.gov.uk/provider/21/136807. Take a minute or two to look at the page.

    There are a couple of things it's worth noting. Firstly, the number at the end of the URL is the school's unique reference number (URN). Try changing the number at the end of the URL to that of another free school - 136808 - and that should confirm this point.

    When you look at that second page, you should notice that it's structured the same way as the previous page.

    These facts - that the URLs follow a pattern, and that pages are structured in a consistent way - are going to be very helpful.

1. Web pages are made up of HTML, meaning that's what you're going to get back when your scraper makes a request to the Ofsted website. To see exactly what you're likely to get back, right click somewhere on the page for the school you were just looking at and select ‘View page source' (wording might differ slightly if you're not using Chrome).

    This shows you the raw HTML that makes up the page. If you're not familiar with HTML, I'd suggest doing some brief reading at this stage to pick up some of the terminology:
    - https://www.w3schools.com/html/html_intro.asp
    - https://www.w3schools.com/html/html_elements.asp
    - https://www.w3schools.com/html/html_attributes.asp
    - https://www.w3schools.com/html/html_classes.asp
    - https://www.w3schools.com/html/html_id.asp

1. Next, you need to find where the inspection rating appears in the HTML. To do this, do `Ctrl + F` while you're viewing the page source and search for whatever the school's most recent rating is (one of 'Outstanding', 'Good', 'Requires Improvement' and 'Inadequate'), and you should see that the rating appears in several places in the HTML.

    One of the places you should see it is a `span` element with the class `nonvisual`. This is a child element of a `h2` element with the class `latest-latest-rating__title`. This might give you a route by which you can find the inspection rating in the HTML - effectively sifting what you want from a lot of stuff you're not interested in

    But it's worth checking – are there other elements in the HTML document with these same classes (`nonvisual`, `latest-latest-rating__title`)? You can do this by using `Ctrl + F` again. The way your scraper works will have to take this into account if there are.

1. Return to your Python code – get rid of the `print` command but keep the first `# %%`. You'll need to load the packages you installed earlier, so add the following immediately after the first `# %%`:

    ``` python
    import requests

    from bs4 import BeautifulSoup
    ```

    Bear in mind in all of this: Python is very fussy about capitalisation and (as you're sure to discover) indentation.

1. Next, in the second cell (i.e. the second set of lines starting with `# %%`) add the following to the cell:

    ``` python
    target_urn = '136807'

    target_url = 'https://reports.ofsted.gov.uk/provider/21/' + str(target_urn)
    ```

    This defines a couple of variables - `target_urn` and `target_url`. You can probably work out what they're doing. And the `str()` bit? That's needed because `target_urn` is of type `int` (integer) - which is different to the type of thing you tried to join it to. Converting `target_urn` to a string solves this problem. If you're not too familiary with Python data types, it's worth reading up on them [here](https://www.w3schools.com/python/python_datatypes.asp) - though don't worry about learning absolutely every type that exists.

    (One thing to note, broadly speaking, in Python strings can be surrounded by either single or double quotes. You'll probably see both used at different points throughout this tutorial.)

1. Run the two cells that you've written so far - you can either run them one-by-one using the `Run Cell` buttons, or run both of them using the `Run Button` at the very top.

    In the output window you should see that both cells have run successfully - there'll be a green tick for each. Unlike for the `print()` statement above there won't be any output for these cells - you're setting things up, but for now you've not asked your script to print anything.

1. The next step is to use the `requests` package which you've imported to request the HTML of `target_url`. In the latest new cell that should have appeared,  add the following, then run this cell (you don't need to run all of the cells again - Visual Studio Code is storing the output of those):

    ``` python
    r = requests.get(target_url)
    ```

1. Next, read the contents of this new variable, `r`, into Beautiful Soup by adding the following line:

    ``` python
    soup = BeautifulSoup(r.content, features='html.parser')
    ```

    You can add this either to the previous cell, or to the latest cell that's appeared at the bottom of your script - it doesn't matter. But once you've added to a cell, run that cell.

1. You can check that the previous step has worked by printing this variable, `soup`.

    To do this, in a fresh cell at the bottom of your script use the `print()` function. But whereas you supplied a [string](https://www.w3schools.com/python/python_strings.asp) to `print()` before when you wrote `print('Hello world')`, you now want to supply a variable (`soup`). See if you can figure out what you need to do - take a good read of that link if you're struggling.

1. You should see that what's printed is similar - nay, the same - as the HTML you saw earlier when you viewed the page source for the school you looked at. (It might not be that nicely formatted, but you should at least be able to see that it starts correctly.)

1. You don't need all of the HTML, though – only the latest inspection rating. This is where Beautiful Soup comes in - you can use it to parse HTML and extract the bits you're interested in.

    You will have seen earlier that there are multiple elements on the page with the `nonvisual` class, one of which is the `span` element that gives the latest inspection rating. This is nested within a `h2` element with the class `latest-latest-rating__title` - and it's the only thing on the page with that class. So it'll be easier to find that element using Beautiful Soup, then move to the child `span` element with the `nonvisual` class than to try and find the correct `span` element to begin with.

    To do that, you can use Beautiful Soup's `find()` function. This finds the first occurence of something in some HTML.

1. To tell the `find()` function where to look, you'll need to supply the name of the `soup` variable. To tell it what to look for, you can tell it to look for a `h2` element with the class `latest-latest-rating__title`. In Beautiful Soup, this is written as:

    ``` python
    soup.find("h2", "latest-rating__title")
    ```

    Why are `h2` and `latest-rating__title` in quote marks? That's because they're strings (which we met above), rather than variables.

1. Let's print the output of this search. So use the `print()` function on it, in the same manner you used `print()` earlier.

1. With any luck, your script will have printed the following - or something similar, depending what the current inspection rating is:

    ``` html
    <h2 class="latest-latest-rating__title">
        <span class="nonvisual">Good</span>
    </h2>
    ```

    Great!

1. You now need to move from having grabbed the parent `h2`, to just having grabbed the `span` element holding the inspection rating which it contains.

    Once you've grabbed a certain chunk of HTML you can move from a parent element to its child element by appending a dot and the type of element you want to move to what you've written previously

    So, start a fresh cell and use the following formulation to select the `span` element we're interested in:

    ``` python
    print(soup.find("h2", "latest-rating__title").<something for you to add>)
    ```

    Jump to the footnotes[^1] if you need the solution.

1. Did that work?

    If so, your `print()` statement should have returned `<span class="nonvisual">Good</span>`, or similar.

    You now need to get the contents of that `span` element - the actual inspection rating.

    Beautiful Soup allows you to get the contents of an element by adding `.contents` to what you've used to select an element.

    So, add `.contents` to the end of what you've written previously, within the `print()` statement. Again, jump to the footnotes[^2] if you need the solution.

1. Hmmm, the square brackets around the output look familiar.

    To confirm what your Beautiful Soup command has returned, replace the `print()` function with the `type()` function.

    Again, you'll find what you should have written in the footnotes.[^3] What you should find is that what Beautiful Soup has returned for you is a Python list, with a single element.

1. You know how to extract the n<sup>th</sup> element from a list - for a list named "my_list" this would be `my_list[n]`. So, see if you can work out what you need to add on to your existing Beautiful Soup commands to extract the inspection rating from the list you've extracted so far. And switch back from using the `type()` function to the `print()` function. See here[^4] for the solution.

1. You've now scraped your first inspection rating!

    For good measure, you can also print the URN of the school you looked up. To print more than one thing using `print()` you supply each thing you want to print to `print()`, separated by commas. You can also supply a separator to `print()`, so the two (or more) things you're asking it to print aren't joined together as a single string.

    So, in a fresh cell, write:

    ``` python
    print(str(target_urn), <your Beautiful Soup code>, sep=" ")
    ```

    This supplies a space (as a string) to `print()`. And the `str(target_urn)` bit? That's because `target_urn` is of type `int` (integer) - that' s

1. This is all great, but one rating alone isn't much. What you could do with doing is looping over a bunch of URNs, and extracting the inspection rating for each.

    Below is a list of five free schools URNs: copy it into your script, create a variable called `target_urns` to hold the list and run the relevant cell.

    ``` python
    [136807, 136808, 136821, 136930, 136934]
    ```

1. In order to iterate over the URNs you'll need to use a `for` loop.

    Now's a good time to read about Python's [`for` loops](https://www.w3schools.com/python/python_for_loops.asp) if you haven't come across them before – in particular, pay attention to the first example, with the list of fruits.

1. Now, in a fresh cell, create a `for` loop that loops over every item in your `target_urns` list and prints the URN.

    If something doesn't work, go back to the link above and double check you've got things like punctuation and spacing/indentation right.

1. Well done if you've got that working.

    The next step is to put the lines of code that go to the Ofsted website and grab the inspection rating in your `for` loop, instead of the `print()` statement. You can keep things like your `import` statements and your definition of `target_urn` outside of the loop, because you only need those things to run once.

    See if you can do this, getting your scraper to print the URN then the inspection rating, separated by a space.

    If you're struggling, see here[^5] for the solution.

1. Some free schools that closed a long time ago no longer have pages on the Ofsted website - for example, [Discovery New School in West Sussex](https://reports.ofsted.gov.uk/provider/21/137326). It's worth thinking about how you'll handle these cases.

    If you take a look at the underlying HTML for that page – ‘View page source' again – you'll see that, perhaps unsurprisingly, it doesn't feature a `h2` element with the `latest-rating__title` class.

    Try changing `target_urns` to a list containing just one element - 137326, the URN for this school - then run your scraper again.

    You'll get a `AttributeError`, which tells you that.

    ``` python
    'NoneType' object has no attribute 'span'
    ```

    What does this mean? It means Beautiful Soup hasn't found what you asked it look for in the page so has returned `None`, which is used to define a null value in Python.

    `None` is of type `NoneType`, so what the error message is telling you is that the result of your `find()` operation (`None`) doesn't have a child `span` element, so Python can't progress with your code.

1. In order to get around this, your scraper will have to behave differently depending whether there is, or isn't, a `h2` element with the `latest-rating__title` class.

    To implement this kind of conditional logic you can use Python's `if...else` statements.

    If you've not come across them before, read about them [here](https://www.w3schools.com/python/python_conditions.asp).

1. See if you can work out the `if...else` statement. (Hint: Your `if` statement will probably want to compare something to the null value `None`, using the formulation `if <something here> is None`.)

    If you can get it working, open [this file](free_school_urns_october_2023.txt), copy the list of URNs there (a subset of primary free school URNs, as of October 2023[^6]) and replace the list that `target_urns` holds with this list.

    If you're struggling, you can find a complete solution [here](scraper_solution.py).

1. Congratulations! You've just written your first Python scraper, using not many lines of code at all.

# Further reading
- [Real Python's guide to web-scraping](https://realpython.com/beautiful-soup-web-scraper-python/)

[^1]: What you should have come up with is `print(soup.find("h2", class_="latest-rating__title").span)`.

[^2]: This time your command should be `print(soup.find("h2", class_="latest-rating__title").span.contents)`.

[^3]: `type(soup.find("h2", class_="latest-rating__title").span.contents)`

[^4]: `print(soup.find("h2", class_="latest-rating__title").span.contents[0])`

[^5]:
    ``` python
    for target_urn in target_urns:
        target_url = 'https://reports.ofsted.gov.uk/provider/21/' + str(target_urn)

        r = requests.get(target_url)
        soup = BeautifulSoup(r.content, features='html.parser')

        print(
            target_urn,
            soup.find("h2", class_="latest-rating__title").span.contents[0],
            sep=" "
        )
    ```

[^6]: Why just primary free schools? URLs for secondary schools are slightly different to those for primary schools on the Ofsted website (and different again for all-through, special and alternative provision free schools). E.g. https://reports.ofsted.gov.uk/provider/23/138245 is the URL for a secondary free school.
