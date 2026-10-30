"""Gói chứa code của từng thành viên."""
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


def load_prompt(name: str) -> str:
    """Đọc prompt gốc trong thư mục prompts/."""
    return (PROMPTS_DIR / name).read_text(encoding="utf-8")
