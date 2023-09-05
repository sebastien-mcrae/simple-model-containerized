from app.models import LongText, SummarizedText
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch

MODEL_PATH = "google/pegasus-cnn_dailymail"


class SummarizationModel:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = PegasusTokenizer.from_pretrained(MODEL_PATH)
        self.model = PegasusForConditionalGeneration.from_pretrained(MODEL_PATH).to(
            self.device
        )

    def run_inference(self, long_text: LongText) -> SummarizedText:
        summary = None
        summary_length = float("+inf")

        text = long_text.text
        max_summary_length = long_text.max_summary_length

        while summary_length > max_summary_length:
            batch = self.tokenizer(
                text if summary is None else summary,
                truncation=True,
                padding="longest",
                return_tensors="pt",
            ).to(self.device)

            summary_ids = self.model.generate(**batch)
            summary_length = len(summary_ids[0])
            summary = self.tokenizer.batch_decode(
                summary_ids, skip_special_tokens=True
            )[0]

            print(f"Summary length: {summary_length}")

        return SummarizedText(summary=summary, summary_length=summary_length)
