from pydantic import BaseModel

EXAMPLE_TEXT = """For the third time in as many months, 
Goldman Sachs has cut the probability that the US economy 
will enter a recession in the next year.
In a note titled "soft landing summer" released Monday, 
Goldman Sachs chief economist Jan Hatzius said there was a 15% chance of a recession
in the next 12 months, down from an earlier forecast of 20%. 
"The continued positive inflation and labor market news 
has led us to cut our estimated 12-month US recession probability," Hatzius wrote.
Goldman Sachs notes its forecast is significantly below Bloomberg's consensus forecast 
for a 60% chance of a recession in the next 12 months.
After a summer of stronger-than-expected economic data, 
Hatzius and Goldman Sachs still see the US economy growing 
at a 2% annual pace on average through the end of 2024."""


class LongText(BaseModel):
    text: str = EXAMPLE_TEXT.replace("\n", "")
    max_summary_length: int = 50


class SummarizedText(BaseModel):
    summary: str
    summary_length: int
