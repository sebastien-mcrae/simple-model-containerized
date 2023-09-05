from fastapi import FastAPI
from app.nlp import SummarizationModel

from . import routes


app = FastAPI()
app.include_router(routes.router)


@app.on_event("startup")
def load_model():
    app.state.summarization_model = SummarizationModel()
