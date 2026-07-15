def print_header(title):
    print()
    print("=" * 40)
    print(title)
    print("=" * 40)


def print_table(headers, rows):
    columns = [headers] + [[str(cell) for cell in row] for row in rows]
    widths = [max(len(col[i]) for col in columns) for i in range(len(headers))]

    def format_row(cells):
        return " | ".join(cell.ljust(width) for cell, width in zip(cells, widths))

    print(format_row(headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_row([str(cell) for cell in row]))


def read_input(prompt):
    return input(prompt).replace("﻿", "").strip()


def read_int(prompt):
    while True:
        value = read_input(prompt)
        if value.lstrip("-").isdigit():
            return int(value)
        print("숫자를 입력해주세요.")


def read_float(prompt):
    while True:
        value = read_input(prompt)
        try:
            return float(value)
        except ValueError:
            print("숫자를 입력해주세요.")
