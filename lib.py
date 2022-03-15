import numpy as np
import os


# Data analyzing
def format_data(data: str) -> list[str]:
    return data.strip().split(",")


def is_id_valid(data: str) -> bool:
    student_id = format_data(data)[0]
    is_valid_length = len(student_id) == 9
    is_valid_digit = all(map(str.isdigit, student_id[1:]))
    return is_valid_length and is_valid_digit


def is_length_valid(data: str) -> bool:
    return len(format_data(data)) == 26


def count_valid(file: str) -> int:
    return sum(
        map(
            lambda line: is_id_valid(line) and is_length_valid(line),
            (line for line in open(file)),
        )
    )


def count_invalid(file: str) -> int:
    return sum(1 for line in open(file) if line.strip()) - count_valid(file)


def student_id(_format_data: list[str]) -> str:
    return _format_data[0]


def student_answer(_format_data: list[str]) -> list[str]:
    return _format_data[1:]


def pairs(
    _formated_key: list[str], _student_answer: list[str]
) -> tuple[tuple[str, str]]:
    return tuple(zip(_formated_key, _student_answer))


def right_answer(_pairs: tuple[tuple[str, str]]) -> int:
    return len(list(filter(lambda item: item[0] == item[1], _pairs)))


def wrong_answer(_pairs: tuple[tuple[str, str]]) -> int:
    return len(list(filter(lambda item: item[0] != item[1] and item[1] != "", _pairs)))


def student_mark(_right_answer: int, _wrong_answer: int) -> int:
    return _right_answer * 4 - _wrong_answer


# write report
def mean(mark_array):
    return np.mean(mark_array)


def median(mark_array):
    return np.median(mark_array)


def range_of_score(mark_array) -> int:
    return abs(max(mark_array) - min(mark_array))


def report(file, mark_array):
    print("*** REPORT ****\n")
    print(f"Total valid lines of data: {count_valid(file)}\n")
    print(f"Total invalid lines of data: {count_invalid(file)}\n")
    print(f"Mean (average) score: {(mean(mark_array)):.2f}\n"),
    print(f"Highest score: {int(max(mark_array))}\n")
    print(f"Lowest score: {int(min(mark_array))}\n"),
    print(f"Range of score: {int(range_of_score(mark_array))}\n"),
    print(f"Median score: {int(median(mark_array))}\n"),


# Dump output
def write_student_result(file, answer_key):
    for line in open(file):
        if not is_id_valid(file) or not is_length_valid(file):
            continue
        else:
            pairs_data = pairs(
                format_data(answer_key), student_answer(format_data(line))
            )
            with open(f"{os.path.splitext(file)}_grades.txt") as f:
                f.write(
                    f"{student_id(format_data(line))},{student_mark(right_answer(pairs_data), wrong_answer(pairs_data))}"
                )


def analyzize(file, answer_key, mark_array):
    print("**** ANALYZING ****\n")
    for line in open(file):
        if not is_length_valid(line):
            print(f"Invalid line of data: does not contain exactly 26 values:\n")
            print(line)
        elif not is_id_valid(line):
            print(f"Invalid line of data: N# is invalid\n")
            print(line)
        else:
            pairs_data = pairs(
                format_data(answer_key), student_answer(format_data(line))
            )
            mark_array = np.append(
                mark_array,
                student_mark(right_answer(pairs_data), wrong_answer(pairs_data)),
            )
    if count_valid(file) == len(list(open(file))):
        print("No errors found!\n")
    return mark_array


def create_output_dir(name="Output") -> str:
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, name)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    return final_directory

def class_result(file, file_name, answer_key):
    with open(
        os.path.join(create_output_dir(), file_name.strip() + "_grades.txt"), "w+"
    ) as f:
        for line in open(file):
            if not is_length_valid(line):
                continue
            elif not is_id_valid(line):
                continue
            else:
                pairs_data = pairs(
                    format_data(answer_key), student_answer(format_data(line))
                )
                f.write(
                    f"""{student_id(format_data(line))},{student_mark(right_answer(pairs_data),
                wrong_answer(pairs_data))}\n"""
                )
