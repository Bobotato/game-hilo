import pytest

import main


@pytest.mark.integtest
def test_quit_at_menu(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "test")
    name = main.get_name()
    assert name == "test"
    monkeypatch.undo()

    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert not main.is_playing()
    monkeypatch.undo()

    with pytest.raises(SystemExit):
        main.end_game()
