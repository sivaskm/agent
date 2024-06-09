import re
import ast
import json
from collections import defaultdict


def get_list(quiz_string):
    match = re.search(r"\[(.*?)\]", quiz_string, re.DOTALL)
    if match:
        quiz_list_string = match.group(0)
        quiz_list = ast.literal_eval(quiz_list_string)
        return quiz_list
    else:
        print("No match found")


def read_json(json_file_path):
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    return data


def organize_data(original_data):
    converted_data = {}

    for item in original_data:
        topic = item["topic"]
        if topic not in converted_data:
            converted_data[topic] = {"topic": topic, "q_and_a": []}

        converted_data[topic]["q_and_a"].append(
            {
                "question": item["question"],
                "correct_answer": item["correct_answer"],
                "selected_answer": item["selected_answer"],
                "difficulty_level": item["difficulty_level"],
            }
        )

    converted_list = list(converted_data.values())
    return converted_list


def get_score(q_and_a):
    total_score = 0
    candidate_score = 0
    for question in q_and_a:
        correct_answer = question["correct_answer"].lower().replace(" ", "")
        selected_answer = question["selected_answer"].lower().replace(" ", "")
        difficulty = question["difficulty_level"].lower().replace(" ", "")
        if difficulty == "easy":
            total_score += 1
            if selected_answer == correct_answer:
                candidate_score += 1
        elif difficulty == "medium":
            total_score += 1.5
            if selected_answer == correct_answer:
                candidate_score += 1.5
        elif difficulty == "hard":
            total_score += 2.5
            if selected_answer == correct_answer:
                candidate_score += 2.5
    return total_score, candidate_score


def convert_to_string(data):
    converted_string = f"Topic: {data['topic']}\n"
    for idx, item in enumerate(data["q_and_a"], start=1):
        converted_string += f"{idx}. Question: {item['question']}\n"
        converted_string += f"   Correct Answer: {item['correct_answer']}\n"
        converted_string += f"   Selected Answer: {item['selected_answer']}\n"
        converted_string += f"   Difficulty: {item['difficulty_level']}\n\n"
    converted_string += f"Total Score: {data['total_score']}\n"
    converted_string += f"Candidate Score: {data['candidate_score']}\n"
    return converted_string
