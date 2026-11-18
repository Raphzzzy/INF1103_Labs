from pathlib import Path

import pytest

from input_helpers import get_positive_float
from main import run_demo


ROOT = Path(__file__).resolve().parents[1]


def test_input_retries_abc_negative_then_accepts(monkeypatch, capsys):
    values = iter(["abc", "-5", "12.50"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))
    result = get_positive_float("Price: ")
    assert result == pytest.approx(12.5)
    assert capsys.readouterr().out == (
        "Please enter a valid number, e.g. 12.50\n"
        "Please enter a number greater than zero.\n"
    )


def test_input_retries_zero_and_infinite(monkeypatch, capsys):
    values = iter(["0", "inf", "3.5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(values))
    assert get_positive_float("Price: ") == 3.5
    assert capsys.readouterr().out.count("greater than zero") == 2


def test_demo_displays_250_bulk_percentage_student_totals(capsys):
    run_demo(str(ROOT / "products.csv"))
    out = capsys.readouterr().out
    assert "Bulk discount total: 230.00" in out
    assert "10% discount total: 225.00" in out
    assert "5% student discount total: 237.50" in out
    assert "P001: Desk Lamp - Ship" in out
    assert "D001: Photo Editor - Provide" in out
