from fastapi import FastAPI

app = FastAPI()
print("Hello , World!!")
GOOGLE_API_KEY="AIzaSyAc7uiC6CoX0cMtGam7Jcuo3cjvRaK30nY"
@app.get("/")
def read_root():
    return {"message": "Render ran successfully, and CI/CD has been implemented."}

@app.get("/api")
def read_root():
    return {"message": "The jenkins ran successfully, and CI/CD has been implemented."}
