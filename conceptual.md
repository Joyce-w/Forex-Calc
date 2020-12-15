### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
  Python users have the capability to import external libraries such as Numpy and SQLAlchemy. Python is also a language which enables coding on the backend. With library extensions, it can be more versatile than JS.
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  
  1. Use dict.get() to return a key and if not, a default can be set.
  2.  dict.setdefault(key,val) also sets a missing key with a corresponding value. 

- What is a unit test?  
  A unit test tests whether each piece of an app is functioning as expected. It is simple and efficient but does not test multiple functions working together.

- What is an integration test?  
  Integration test combine multiple functions together. In flask a virtual server can be arranged to do integration testing.0000

- What is the role of web application framework, like Flask?  
  Frameworks are more thurough than libraries because they provide more functionality and rules to follow in order to set up where files should go and how an application should look like. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
 For basic paths using a route URL woul be ideal. In cases, where a search or filtering is required, a query param should be used. 
- How do you collect data from a URL placeholder parameter using Flask?

- How do you collect data from the query string using Flask?  
  There is a request method that can be used to collect data. (i.e. request.args.get(<name_of_query>)).

- How do you collect data from the body of the request using Flask?  
  request.data() gets data from the body in Flask. 
- What is a cookie and what kinds of things are they commonly used for?  
  Cookies are stored in the browser and sends information to a site when a http methods is being used. Information such as browsing content is often stored.

- What is the session object in Flask?  
- Session is similar to cookies and stores information but on the client side and in larger capacity. It only lasts as long as the browser is open.

- What does Flask's `jsonify()` do?  
  jsonify() wraps a response object into an application/json type. This allows for easier data handling. 
