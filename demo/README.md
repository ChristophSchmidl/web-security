# Demo webpages for Web Security

This directory contains some examples that illustrate some features of the web (or more in particular, of HTTP and HTML), including
* GET and POST requests
* mixing HTTP and HTTPS content
* javascript
* the DOM (Document Object Model)
* the SOP (Single Origin Policy)
* the use of frames, and ways to abuse these, for instance for ClickJacking

Note that the file README.html is included automatically by the webserver if you ask for a directory listing of http://www.cs.ru.nl/~erikpoll/websec/demo.
The demos in this directory are:

The demoes in this directory are:

* demo_get_post.html is a page with GET and POST requests.
* mixed_content.html is a page which mixes HTTP and HTTPS content.
* demo_javascript.html is a page with simple JavaScript to create an alert window.
* demo_DOM.html is webpage with some buttons that invoke javascript functions to interact with the webpage using the DOM (Document Object Model).
* test_SOP.html and test_SOP2.html are pages with inner frames that test the Single Origin Policy (SOP),
* Web pages with ClickJacking/UI redressing: clickjack_basic.html , clickjack_some_button.html clickjack_some_button_transparent.html
* The Clickjacking examples clickjack_bb_using_UI_redressing.html and clickjack_radboudnet_using_UI_redressing.html attempt UI redressing on Blackboard.ru.nl and Radboudnet.nl, but these might not work depending on your browser settings. For instance, Blackboard uses javascript for frame busting, so the example will only work with javascript turned off; or else you can see the effect of the frame busting. Also, if you're not logged on to Blackboard resp. Radboudnet they might not look as intended.
* The more fancy Cursor clickjacking attack shows shows how the attacker can confuse the user about where the cursor really is, and hence about what he is clicking.