# Api Planetarium project

API Planetarium is a  project helps visitors to book tickets online for their favourite ShowSessions in local Planetarium.

-------------------------------------------------------------------------------------
## Features

- **Show Themes Management** : Manage different themes for astronomy shows, allowing customization and thematic variety for each presentation.
- **Planetarium Dome Configuration** : Configure and manage multiple planetarium domes, including seating arrangements and dome specifications.
- **Astronomy Shows**: Create, update, and list astronomy shows with details such as title, description, duration, and associated themes.
- **Authenticated Access**: Restrict access to certain features, ensuring only authenticated users or staff members can perform specific actions.
- **Booking System**: Facilitate the booking of shows and manage reservations within the planetarium.
- **API Endpoints**: Provide REST API endpoints for accessing and managing data related to show themes, domes, and shows.
- **User Authentication**: Support user login and registration to access personalized features.
- **Administrative Control**: Allow administrators to manage show details, dome configurations, and user permissions.

-------------------------------------------------------------------------------------

## API Reference

#### Before start using this API Project, u should use register(if not yet) or use JWT Token for authentification if u already register.

#### For register:

```http
  POST api/user/register/
```
| Key | Type     | Description                |
| :-------- | :------- | :------------------------- |
| Email | Email | Required. Your Email |
| Password | Password | Required. Your Password |

#### For authentification (you should use your credentetials for authentification)

```HTTP
  GET api/user/token/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| Email    | Email | Required. Your Email |
| Password    | Password | Required. Your Password |

### You can see information about your account inc. email, are you staff etc. (update account info as well)


```HTTP
  GET api/user/me/
```
------------------------------------------------------------------------------------

## RESOURCES

Note: You can get further resources if you are authenticated

#### Get list of Show Themes and create new one (if you have admin permissions)

```HTTP
   GET /api/planetarium/show_theme/
```
#### Get list of Show Sessions and create new one (if you have admin permissions)

```HTTP
   GET /api/planetarium/show_session/
```
#### Get list of Planetarium Domes and create new one (if you have admin permissions)

```HTTP
   GET /api/planetarium/planetarium_dome/
```
#### Get list of Astronomy Shows and create new one (if you have admin permissions)

```HTTP
   GET /api/planetarium/astronomy/
```
#### Update current theme (possible if user has admin permissions)
```HTTP
   PUT, PATCH or DELETE(in admin) /api/planetarium/show_theme/{id: int}/
```
#### Update current show session (possible if user has admin permissions)
```HTTP
   PUT, PATCH or DELETE(in admin) /api/planetarium/show_session/{id: int}/
```
#### Update current planetarium dome (possible if user has admin permissions)
```HTTP
   PUT, PATCH or DELETE(in admin) /api/planetarium/planetarium_dome/{id: int}/
```
#### Update current astronomy show (possible if user has admin permissions)
```HTTP
   PUT, PATCH or DELETE(in admin) /api/planetarium/astronomy/{id: int}/
```
-----------------------------------------------------------------------------------
### Create reservation for you
```HTTP
   GET /api/planetarium/reservation/
```

----------------------------------------------------------------------------------
## Admin Panel

#### You can join admin panel through this endpoint:
```HTTP
GET /admin
```
*Example*: http://127.0.0.1:8000/admin/

#### Information about superuser:


| *Parameter* | *Type*          | 
|:------------|:----------------|
| Email       | admin@gmail.com |
| Password    | python123       |
----------------------------------------------------------------------------------
```
