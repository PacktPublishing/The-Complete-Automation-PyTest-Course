def greeting(name):
    print('Hello,', name)


def test_greeting(capfd):
    greeting('Martin')
    out, err = capfd.readouterr()
    assert out == 'Hello, Martin\n'


def test_multiline(capfd):
    greeting('Martin')
    greeting('Petya')
    out, err = capfd.readouterr()
    assert out == 'Hi, Martin\nHi, Petya\n'


def test_disabling_capturing(capfd):
    print('capturing output')
    with capfd.disabled():
        print('missed output')
    print('on ther captured output')
