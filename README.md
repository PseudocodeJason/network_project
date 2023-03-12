# network_project

Next step
- Implement the API
- Create pages to input the user name and message. Those information is allow to insert to the database


data model 
User Table:
- user_id (primary key)
- name

Chat Message Table:
- message_id (primary key)
- user_id (foreign key to User Table)
- message_text
- timestamp

Response Table:
- response_id (primary key)
- message_id (foreign key to Chat Message Table)
- response_text
- timestamp

![image](https://user-images.githubusercontent.com/32995324/224576907-ed523d62-7d2f-447c-a05b-b57d8f4bd262.png)
![image](https://user-images.githubusercontent.com/32995324/224576940-06b70bb2-33f7-48ed-be47-2be2d48ca5f9.png)
![image](https://user-images.githubusercontent.com/32995324/224576951-7cb84b5f-c27a-4569-803f-8e545f0adb5b.png)

