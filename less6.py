import urwid


def on_ask_change(edit, new_edit_text):
    password = new_edit_text
    score = calculate_score(password)
    score_text.set_text(f"Рейтинг пароля: {score}")

def calculate_score(password):
    score = 0
    checks = [
        has_digit,
        is_very_long,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]

    for check in checks:
        score += check(password)

    return score

def has_digit(password):
    return 2 if any(char.isdigit() for char in password) else 0

def is_very_long(password):
    return 2 if len(password) > 12 else 0

def has_letters(password):
    return 2 if any(char.isalpha() for char in password) else 0

def has_upper_letters(password):
    return 2 if any(char.isupper() for char in password) else 0

def has_lower_letters(password):
    return 2 if any(char.islower() for char in password) else 0

def has_symbols(password):
    return 2 if any(not char.isalnum() for char in password) else 0

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

def main():
    global score_text

    ask_text = urwid.Text("Введите пароль:")
    ask_edit = urwid.Edit()
    score_text = urwid.Text("Рейтинг пароля: 0")

    urwid.connect_signal(ask_edit, 'change', on_ask_change)

    pile = urwid.Pile([ask_text, ask_edit, score_text])
    top = urwid.Filler(pile, valign='top')

    loop = urwid.MainLoop(top, unhandled_input=exit_on_q)
    loop.run()

if __name__ == '__main__':
    main()