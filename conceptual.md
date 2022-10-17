### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

*Python used for the backend while JavaScript can be used for both the back-end and the front end.
*There are differences in syntax and the strictness of Python vs JavaScript
..*JavaScript tends to be less opinionated than Python
..*Python relies on indentation to define code blocks while JavaScript uses curly braces.
..*Variables are definied differently and have different mannerisms. Variables in Python are written variable followed by name and all are function-scoped. In JavaScript, variable names follow a keyword and based on that key word have different properties.
..*Naming conventions between the two are different. Python leans towards snake case, while JavaScript leans towards using camel case.
..*When indicating a variable doesn't have a value, Python calls it None while JavaScript calls it null and has undefined as a special value as well.
..*In JS, empty arrays and objects are considered truthy. Python considers all empty data structures as falsy.
..\*JavaScript equality has two different syntax. "==" for loosely equal. "===" for strictly equal. Python has "==" for strictly equal.
..\*And, or, not are written differently. Python writes them "and , or, not". JavaScript writes them "&& , || , !"

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your program crashing.

1. You can use the .get method. If key is present in the dictionary, then value will be provided, but if it is not, it will not care and return a message provided as the def_val

2. Pull out using .keys method and check if missing key is in the key.

- What is a unit test?

\*Test that checks that a single compment such as a function or method works in the right way. Meant to isolate individual components and check to see if those individual components work like expected independent of any other component.

- What is an integration test?

\*Test that multiple components work together. Example of use cases would be checking if the URL path map to the correct route function. Has the expected information been passed.

- What is the role of web application framework, like Flask?

*Role is to support developers by providing a library to handle basic details and hide any complexities of common web development tasks. Makes it easier to write, maintain, and scale web applications.
*Flask helps with defining which requests to respond to or how to respond to requests and etc.
\*Web application frameworks help make it easier to work with requests and responses, storing and retrieving sessions, provide otuput formats with a templating engine.

- You can pass information to Flask either as a parameter in a route URL (like
  `/foods/pretzel`) or using a URL query string param (like
  `foods?type=pretzel`). How might you choose which one is a better fit for an
  application?

*If using POST, then will use parameter in the route URL.
*Parameter in a route URL when you want it to feel like the subject of the page. Query Parameter when you want to show the information that is being passed in such as when data is coming from a form.

- How do you collect data from a URL placeholder parameter using Flask?

\*Pass it in through the parameters when calling function. Use request.args or .form depending on if it is a form to call the name of the object key and get the value.
\*After using request.args, can convert to a regular dictionary or look for specific key.

- How do you collect data from the query string using Flask?

\*can collect information using .get() method or call it in the parameters when function is called.

- How do you collect data from the body of a POST request using Flask?

\*Using request.get_json(), we now have access to the data.

- What is a cookie and what kinds of things are they commonly used for?

*Cookies are name/string-value pairs. It is a piece of data from a website that is stored within the web browser so that website can hold onto and retrieve that data at a later time.
*Commonly used to help the website remember information about your visit so that next time you visit or while you are visiting, it can help with your visit.

- What is the session object in Flask?

*A dictionary object that contains a key-value pair for session variables and associated values.
*It contains information for the current browser and preserves types.
\*Sessions are stored in the browser as cookies and are serialized and signed.

- What are the two things Flask's `jsonify()` does?

*serializes data to JSON format
*wraps it in a response object

- What was the hardest part of this past week for you?
  What was the most interesting?

  *Actually seeing how to connect the backend and making something out of it was interesting and hard to understand. Hardest part was categorizing the roles of Flask and the individual components of them similar to APIs and AJAX. The biggest learning curve I am on is with understanding how they really interact with each other and optimize their use cases.
  *Specific interests were imagining the possibilities with backend and getting to understanding the idea of databases and data structures. Accessing information and manipualting the information to produce something specialized.
