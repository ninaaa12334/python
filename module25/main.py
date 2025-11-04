import database
import models

app = FastAPI()
@app.get("/")
def read_root():