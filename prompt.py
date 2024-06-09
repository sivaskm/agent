def get_pre_rqst_msgs(topic):
    resp_json = {
        "name of pre-requisite-1": "description of pre-requisite 1",
        "name of pre-requisite-2": "description of pre-requisite 2",
    }

    system_msg = f"""You are a personalized learning assistant.
  You help users to find the list of pre-requisites to learn before delving into a particular topic.
  You would call suitable tools when needed and use outputs from tools to better assist the users in finding the pre-requisites.
  You are capable of communicating only in valid JSON format with no other text.
  Your response should be in the below JSON format.
  {resp_json}
  """

    user_msg = f"""Give me a list pre-requisites to learn before learning {topic}
  Use web search when required.
  Give only the topic name in web search.
  Analyse those web search results, and then you prepare the list of pre-requisites.
  Give atmost one pre requisites.
  """

    return [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg},
    ]


def get_quiz_msgs(topic):
    resp_json = [
        {
            "question": "What is the capital of India",
            "correct_answer": "New Delhi",
            "other_options": ["Chennai", "Banglore", "Kolkata", "Mumbai"],
            "diificulty_level": "medium",
        },
        {
            "question": "What is the current GDP of India",
            "correct_answer": "USD 3.75 trillion",
            "other_options": [
                "USD 1.75 trillion",
                "USD 2.25 trillion",
                "USD 3.7 trillion",
                "USD 3.75 billion",
            ],
            "diificulty_level": "hard",
        },
    ]

    system_msg = f"""You are a quiz creation assistant.
  You would call suitable tools when needed and use outputs from tools to create better quiz.
  Use web search only if you are not familiar with the topic.
  You are capable of communicating only in valid JSON format with no other text.
  Your response should be in the below JSON format. Always use double quotes for string values.
  Don't give any other text except the result JSON.
  {resp_json}
  """

    user_msg = f"""Prepare a quiz with six questions about {topic}. Two questions should be easy, two should be medium and two should be hard.
  Use web search when required. Use only one tool with a generic query. Analyse that result and generate questions from it.
  For each question give below details:
  1. question: Well written detailed question
  2. correct_answer: Correct answer to the question
  3. other_options: List of options to give with the correct answer. Should be sementically similar to the correct answer. Correct answe should not be in this list.
  4. diificulty_level: easy or medium or hard
  """

    return [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg},
    ]


def get_eval_msgs(result):

    system_msg = f"""You are a quiz evaluation assistant.
  You help users to know about their strenghts and weaknesses based on their quiz result.
  Only give quiz evaluation with no other text.
  """

    user_msg = f"""Evaluate my following quiz.
  {result}
  """

    return [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg},
    ]
