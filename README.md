# HW2 by Irina Shekhovtsova (412693)

Authentication form is rendered at http://localhost:5000/login. When user goes to http://localhost:5000/, authentication form is also rendered with the help of redirect.
<br> If successfully authenticated, profile page is rendered. Profile page shows for authenticated user only at http://localhost:5000/profile
<br> There is also a registration form that is available at http://localhost:5000/register.
<br> User can exit at http://localhost:5000/logout.
<br>Username and hash password are stored in Mongodb
<br> To handle web forms the Flask-WTF extension is used
<br> To manage users Flask-Login is used
