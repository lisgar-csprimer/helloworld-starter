def test_main(capsys):
    import main
    capture = capsys.readouterr()
    assert capture.out == "Hello World!\n"
