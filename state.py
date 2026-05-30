from typing import TypedDict


class EssayState(TypedDict):
    essay: str

    language_result: str
    analysis_result: str
    clarity_result: str

    avg_score: float
    final_report: str