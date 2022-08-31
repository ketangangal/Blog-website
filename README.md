## Blog Website
Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. 
Built by experienced developers, Django takes care of much of the hassle of web development, 
so you can focus on writing your app without needing to reinvent the wheel.

## Blog app interface
![image](https://user-images.githubusercontent.com/40850370/187646882-e20c3ae0-09c7-46b3-be22-dc362dddbe24.png)

![image](https://user-images.githubusercontent.com/40850370/187647376-d11d2bdc-80c9-43a0-aca5-cb49b74c1960.png)

![image](https://user-images.githubusercontent.com/40850370/187647542-19278b4e-339b-41f5-b570-dbaa3ca107d9.png)

![image](https://user-images.githubusercontent.com/40850370/187646581-a9c66093-4a39-4c62-936c-a9d9d55505ff.png)

## How to Setup 
How to run the project :

1. Create new Environment with python 3.7 
2. Install requirements.txt
3. Create super user using command
  
```python
python manage.py createsuperuser
```    
4. Enter new username and password 
5. Now run the server using command 
```python
python manage.py runserver
```    
6. Go to url 127.0.0.1:8000/admin now login with your username and password
7. Now go to social applications and click on add social application on right hand side 
8. Now go to GCP console and create new project > APIs & Services > oAuth consent screen > add new app > Credentials > OAuth 2.0 Client IDs > copy client id and secret key 

![Screenshot1](https://user-images.githubusercontent.com/31993185/162887474-0a17fe19-1e90-4d5b-8d3e-b0b64e95fb6e.png)

9. Write http://127.0.0.1:8000 in Authorised Javascript origins 
10. Write http://127.0.0.1:8000/accounts/google/login/callback/ in Authorised redirect URls
11. Now go back to your 127.0.0.1:8000/admin portal and under social application write down the required client id and secret key and all other details as shown in the image 
![Screenshot 2](https://user-images.githubusercontent.com/31993185/162888206-0ddf462d-98b7-432b-bf98-75b1ea1f6836.png)
12. Now go to Sites sections and write down these details shown in image 
![Screenshot 3](https://user-images.githubusercontent.com/31993185/162888415-390a7be7-1207-4b8b-9fc3-76311a663e2b.png)
13. Your google verification is successfully done now you can run your application using 
```python
python manage.py runserver
```
## Tech Stack 
1. python 
2. Django 
3. Html 
4. Css

## Conclusion 
To get hands on learning on the django framework we, have build a blog website. 