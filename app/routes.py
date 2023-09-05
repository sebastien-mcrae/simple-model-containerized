from fastapi import APIRouter
from starlette.requests import Request
from app.models import LongText, SummarizedText

router = APIRouter()


@router.get("/")
def health():
    return {"status": "ok"}


@router.post("/summarize")
def summarize(request: Request, long_text: LongText) -> SummarizedText:
    summarization_model = request.app.state.summarization_model
    return summarization_model.run_inference(long_text)
