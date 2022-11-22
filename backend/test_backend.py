import requests

def post_ventas_data(): 
   url = 'http://custom_server.localhost:5000/record/post_ventas' 
   obj = {
	"transaction_id":"48182",
	"description": "description1",
	"value": 204,
	"transaction_date": "2/20/2022"
    }
   requests.post(url, json = obj)
   obj = {
	"transaction_id":"48183",
	"description": "description2",
	"value": 1029,
	"transaction_date": "2/20/2022"
    }
   requests.post(url, json = obj)
   obj = {
	"transaction_id":"48184",
	"description": "description3",
	"value": 1090,
	"transaction_date": "2/20/2022"
    }
   requests.post(url, json = obj)
   url = 'http://custom_server.localhost:5000/record_middleware/get_all'
   headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlRfTWF1cm9fMDE5IiwiZW1haWwiOiJtYXVyaW5yaW5yaW5AZ21haWwuY29tIiwiZXhwIjoxNjY5MjE0NTkyfQ.GSHs0G_q0_xCDx4Is2tvgFKd3IGSl8bZnG3BDsIPIng"}
   return requests.get(url, headers=headers).json()

def post_all_data(): 
   url = 'http://custom_server.localhost:5000/record_all/post_record' 
   obj = {
	"transaction_id":"111",
	"description": "description1",
	"value": 204,
	"transaction_date": "2/20/2022"
    }
   requests.post(url, json = obj)
   obj = {
	"transaction_id":"112",
	"description": "description2",
	"value": 1029,
	"transaction_date": "2/20/2022"
    }
   requests.post(url, json = obj)
   obj = {
	"transaction_id":"113",
	"description": "description3",
	"value": 1090,
	"transaction_date": "2/20/2022"
    }
   requests.post(url, json = obj)
   url = 'http://custom_server.localhost:5000/record_all_middleware/get_all'
   headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlRfTWF1cm9fMDE5IiwiZW1haWwiOiJtYXVyaW5yaW5yaW5AZ21haWwuY29tIiwiZXhwIjoxNjY5MjE0NTkyfQ.GSHs0G_q0_xCDx4Is2tvgFKd3IGSl8bZnG3BDsIPIng"}
   return requests.get(url, headers=headers).json()

def check_post(id_data, json_data): 
    for i in range(len(json_data)):
        if (json_data[i]["transaction_id"]) == id_data:
            return True
    return False 

def check_post_all_rule(): 
    url = 'http://custom_server.localhost:5000/record_all/post_record' 
    obj = {
	    "transaction_id":"111",
	    "description": "description4",
	    "value": 2094,
	    "transaction_date": "2/20/2022"
    }
    return requests.post(url, json = obj).status_code

def check_post_ventas_rule(): 
    url = 'http://custom_server.localhost:5000/record/post_ventas' 
    obj = {
	    "transaction_id":"48182",
	    "description": "description4",
	    "value": 501,
	    "transaction_date": "2/20/2022"
    }
    return requests.post(url, json = obj).status_code

def test_answer1():
    assert len(post_ventas_data()) == 3

def test_answer2():
    assert len(post_all_data()) == 3

def test_answer3():
    assert check_post('193', post_all_data()) == False 
    assert check_post('112', post_all_data()) == True 

def test_answer4():
    assert check_post('48184', post_ventas_data()) == True 
    assert check_post('112', post_ventas_data()) == False 

def test_answer5():
    assert check_post_all_rule() == 400 

def test_answer6():
    assert check_post_ventas_rule() == 400 


url = 'http://custom_server.localhost:5000/account/login'
myobj = {
        "username":"T_Mauro_019",
	    "password":"329|=XOO"
        }
x = requests.post(url, json = myobj)
#print(x.text)

