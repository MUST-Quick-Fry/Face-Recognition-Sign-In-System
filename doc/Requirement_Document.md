## Requirement Document
### Existed Problem
  1. Traditional sign in methods like using apps is easy to forget, our software seems more convenient.
  2. Cannot record the period of class, some students may leave the class in the middle, but we can do this now.
  3. Signing in with a fake person may take place, but our recognition system can avoid it.
  4. App maintenance will influence the sign in system.  If we use independent software, the impact will decrease.
### Background Info
Face recognition is now widely used in large companies. It is a relatively mature and flexible technology which can be applied in our campus to consummate functions.
<!-- Use case UML here!! -->
### Environment & System Modules
  + Face Recognition Module 

    This module is based on flexible and encapsulated API built by machine learning and deep learning  
  + Registration and Verification Module
        

  + Client & Webpage
  
    Visible interaction tools are designed for users and administrators 
### Functional Requirements
  + Face recognition
  
    + precise recognition and verification 
    + instant feedback message (including windows message)
      
  + Registration and Storage
  
    Freshmen can register in client or website, and see the results through Wemust app. 
  + Management and Administration
  
    Administrator (teacher) is allowed to login and visit the webpage, to modify and update 
### Non-functional Requirements
+ Environment and Platform requirements 
  + Language : python 
  + Frontend framework : Django

    supports the latest stable release (except where noted) of these browsers:
    + Chrome 
    + Firefox
    + Microsoft Edge
    + Safari 
    > Note: Prerelease ( such as Beta) versions of operating systems and browsers are not supported.
  + Backend & database : sqlite
  + Client UI design : PyQt 
  + Cloud deployment (recommended but not compulsory)   
+ Quality requirements 
  
  + Database capacity: Around 3000 (lite)
  + Short time delay and response
  + Internet connection
    + Upload : 5 Mbps
    + Download : 5 Mbps 
  + Regular maintenance
  + Stability and Security
+ Process requirements 
  + OOP Coding 
  + Open-source hosting platform : Github

