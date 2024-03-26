from fastapi import FastAPI,HTTPException
import uvicorn

app = FastAPI()

students = {
    "fadilla":{
        "hobi":"membaca",
        "makananfavorit":"bakso",
    },"kumala":{
        "hobi":"menyanyi",
        "makananfavorit":"mie"
    },"putra":{
        "hobi":"main valo",
        "makananfavorit":"nasi"
    }
}

#base url (homepage)
@app.get("/") #'/' setara dengan base url

def home():
    return {"message": "Hello World"}

# cara jalanin di terminal uvicorn apipart1:app --reload

#msg lain
@app.get("/sby4message") 

def msg():
    return {"message": "fsds batch sby4 gudluking"}

#show students data
@app.get("/sby4") #'/sby4' berarti end-point baru

def sby4():
    return students #panggil variabel

#show one student data
@app.get("/{name}") #

def getName(name:str):
    if name in students.keys():
        return students[name]
    else:
        raise HTTPException(status_code=404, detail="students not found, try this (fadilla,kumala,putra)")
    
#Add students data (POST)
@app.post('/add_data')

def addData(studentsData:dict):
    print('Students Data : ',studentsData)
    studentsName = studentsData['name']
    studentsHobi = studentsData['hobi']
    studentsMakanan = studentsData['makananfavorit']
    #add to data
    students[studentsName] = {
        "hobi":studentsHobi,
        "makananfavorit":studentsMakanan
    }
    #add message
    return{"message":"Students data have successfully added"}

# if __name__=="__main__":
#     uvicorn.run('apipart1:app',host="127.0.0.1",port="8000", reload=True)