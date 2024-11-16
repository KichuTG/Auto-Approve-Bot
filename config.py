from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "your api id"))
    API_HASH = getenv("API_HASH", "your api hash")
    BOT_TOKEN = getenv("BOT_TOKEN", "7553314720:AAFEEqWejYdZjJZTt2IXan-WNKt1Vz1wuFA")
    FSUB = getenv("FSUB", "Dramaship")
    CHID = int(getenv("CHID", "-1002039807510"))
    SUDO = list(map(int, getenv("1350212613 1905251964").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://jiosaavn:jiosaavn@cluster0.ouhhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
