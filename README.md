# network_project
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

