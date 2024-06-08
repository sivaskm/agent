import json
from config import model
from llm import client
from prompt import get_pre_rqst_msgs, get_quiz_msgs
from tools import web_search, web_search_tool, available_functions
import random

def run_conversation(messages, tools, available_functions):
    response = client.chat.completions.create(
        model=model, messages=messages, tools=tools, tool_choice="auto", max_tokens=4096
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        messages.append(response_message)
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(query=function_args.get("query"))
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )
        second_response = client.chat.completions.create(model=model, messages=messages)
        try:
            return json.loads(second_response.choices[0].message.content)
        except Exception as e:
            print(e, second_response.choices[0].message.content)
         
    else:
        try:
            return json.loads(response_message.content)
        except Exception as e:
            print(e, response_message.content)
    

def get_quiz(topic):
    pre_rqsts = run_conversation(get_pre_rqst_msgs(topic=topic), [web_search_tool], available_functions)
    pre_rqsts[topic] = ""
    total_questions = []
    for topic in pre_rqsts:
        print(topic)
        try:
            questions = run_conversation(get_quiz_msgs(f"{topic}: {pre_rqsts[topic]}"), [web_search_tool], available_functions)
        except Exception as e:
            print(e)
            continue
        for question in questions:
            question["topic"] = topic
        total_questions.extend(questions)
    
    formatted_questions = []
    for question in total_questions:
        all_options = question["other_options"] + [question["correct_answer"]]
        random.shuffle(all_options)
        original_question = question.copy()
        del original_question["other_options"]
        original_question["all_options"] = all_options
        formatted_questions.append(original_question)
    return formatted_questions
