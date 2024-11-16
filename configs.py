from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28714959"))
    API_HASH = getenv("API_HASH", "c0b9797634090ee3f4c1c56db6c051a7")
    BOT_TOKEN = getenv("BOT_TOKEN", "7553314720:AAFEEqWejYdZjJZTt2IXan-WNKt1Vz1wuFA")
    FSUB = getenv("FSUB", "Dramaship")
    CHID = int(getenv("CHID", "-1002039807510"))
    SUDO = list(map(int, getenv("1905251964"))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://jiosaavn:jiosaavn@cluster0.ouhhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
