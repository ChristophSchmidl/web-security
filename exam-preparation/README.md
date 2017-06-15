# Exam Preparation

## Mock Exam (english version)


1. Why is it a better idea to use rather a POST than a GET request when some paramters are confidential, although it is possible for an attacker who eavesdrops the network traffic to inspect the data in both cases?

	* Answer

2. How does HSTS work? Also try to explain what attacks HSTS tries to prevent and how.

	* Answer


3. What is the difference between a normal and a blind SQL injection?

	* Answer


4. Is CSRF abusing the trust of a website in to the user or the trust of the client/user in the website? Elaborate your answer.

	* Answer


5. XSS attacks also use CSRF from time to time.	Draft an example of a XSS attack where CSRF is not used en an example of a XSS attack where CSRF is used as well.

	* Answer


6. 


	* ```
		<html><body>
		<iframe src="http://xx.com/x.html"> </iframe>
		<input type="button" value="Roep f aan op iframe above"
			onclick="frames[0].f();">
		</body></html>

	* a) Under which requirements is the invocation	of f allowed and when is it not allowed?

		* Answer

	* b) What is the motivation for such requirements/conditions based on a security perspective? With other words, which kinds of attacks are these requirements trying to prevent?

		* Answer



7. What is the difference between a "secure" cookie and an "HttpOnly" cookie?

	* Answer



8.  * a) What is a path traversal a.k.a file name injection attack?

		* Answer

	* b) Name at least 10 counter measures against this kind of attacks and also explain how it works.

		* Answer


9. SSL stripping makes it possible for an attacker to break up an HTTPS tunnel between the browser and the server and exchanging (i) a HTTP connection between the browser and himself and a HTTPS connection btween himself and the server or (ii) a HTTPS connection between the browser and himself and a HTTPS connection between himself and the server. What are advantages and disadvantages of the first case in contrast to the second case based on the perspective of the attacker?

	* Answer



10. How does a Remote File Inclusion attack work against a PHP web application?

	* Answer


11. Assume someone has no Facebook-account. Is it possible that there is still a privacy risk where information is leaking towards Facebook?
	Elaborate your answer. Explain why there is a risk or why there is no risk. If there is a risk, explain what kind if information could leak and what the user could do against it.

	* Answer


12. This question is about the WebGoat assignment to spoof an authentication cookie.

	* ![AuthenticationCookie](img/12.PNG)	
	* When you login on this website with the username "webgoat" and password "webgoat", the server sets a session cookie with the value "AuthCookie=65432ubphcfx". When you logout and then login again with the username "aspect" and password "aspect", then the value of the cookie gets set to "AuthCookie=65432udfqtb".
	How can you login as user "bob" without actually knowing his password? Which tools are required to execute this attack and how does it work?

		* Answer	


13. Two of the assignments on websecurity.cs.ru.nl had the goal to steal a cookie. Explain briefly the steps which are required for this attack and which kind of infrastructure the attacker needs.
	
	* Answer		
