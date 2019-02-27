# Sending_data_from_html_form_to_python_flask  
![insert](https://user-images.githubusercontent.com/47202519/53413964-90c24e00-39f3-11e9-98d2-453835d257b3.jpg)

## Key features for HTML  page
<ol>
  <li>We create a front end page in <strong>HTML language</strong>,in this page we define a name, password, email, phone with a text field.</li>
  <li>On submit,<strong>from action</strong> will send the form data to a file named or link <strong>"http://localhost:5000/login"</strong> (to process the input)</li>
  <li><strong>method attribute</strong> specifies how to send form-data. The form-data is sent to the page specified in the action attribute.Value of method = POST or GET.</li>
  <li>The <strong>GET method</strong> used to send as URL variable and length of a URL is limited about 3000 characters. Never use GET to send sensitive data because data will be visible in the URL.</li>
  <li>The <strong>POST method</strong> is used to send form data inside the body of the HTTP request and data is not shown in URL</li>
  <li>In the <strong>password field </strong>, we define a <strong>input pattern attribute</strong> in which we can define the condition for a password, this condition will contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters.</li>
  <li>To show the password, we used a<strong> checkbox attribute</strong> in which a password will be visible. With the help of <strong>javascript</strong>,the <strong>script tags</strong> use to define the condition for a checkbox. </li>
  <li>Now to select a gender, we used a <strong> radio button</strong> with values.  </li>
  <li>We create a field for email, in which <strong>input pattern attribute</strong> is use to define a format for email. Format will be <strong>@gmail.com</strong>. If an email does not match with a pattern it will show the <strong>title</strong> message. </li>
  <li>In phone code, we used a <strong>select tag</strong> for drop-down list and <strong>option tag</strong> for a number of options.</li>
  <li>In the phone filed,the <strong>input pattern attribute</strong> is used to define a regular expression. [7896] the number will start from 9 or 8 or 7 or 6, in second part [0-9] we can enter any number between 0 to 9. last part will indicate {9} index number it will be from 0 to 9 only 10 number.</li>
  <li>To submit your form, use the<strong> submit button</strong> and close all the tags of the HTML document.</li>
  </ol>  
  
  ![htmldow](https://user-images.githubusercontent.com/47202519/53476378-41822900-3a98-11e9-98f2-503d4f1155d6.png)
  
  
  ## Key feature for python page
  <ol>
  <li>we use flask in the backend to make a connection between the HTML page and python page. flask is a web application framework and written in python.</li>
  <li><strong>import flask</strong> module in the project is a mandatory object of flask class  </li>
  <li>To make a connection with the database, we need to <strong>import MySQL connector</strong></li>
  <li>flask constructor takes the name of the current module (__name__) as an argument</li>
  <li>The <strong>route()</strong>function of the flask class is a decoder, which tells the application which URL should call the associated function</li>
  <li>In the <strong>@app.route()</strong>, we also define the methods to send data. MethodS will be the same as in the HTML page. </li>
  <li>If methods= ['POST']  
    syntax of request method is  
    if request.method == 'POST':# request method to use 'POST'
      username = request.form['username']# syntax to use get() method &&&&
      password = request.form['password']
      gender = request.form['Gender']
      email = request.form['email']
      phonecode = request.form['phonecode']
      phonecode=str(phonecode)
      phone = request.form['phone']
      phone=str(phone)</li>
  <li></li>
  <li></li>
</ol>
