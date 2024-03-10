from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("hello", 3) == "leh_ol"
    assert encrypt_message("hello", 2) == "oll_eh"
    assert encrypt_message("hello", 8) == "olleh"
    with pytest.raises(TypeError):
        encrypt_message(123, 3)
    with pytest.raises(TypeError):
        encrypt_message("hello", "key")
    assert encrypt_message("hello", 20) == "olleh"
