REGISTER_SCHEMA = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "institution": {"type": "string"},
        "role": {"type": "string", "enum": ["Admin", "Teacher", "Student"]},
    },
    "required": ["username", "password", "email", "institution", "role"],
}

LOGIN_SCHEMA = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["username", "password"]
}

RESET_PASSWORD_SCHEMA = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "password": {"type": "string"}
    },
    "required": ["user_id", "password"]
}

ADMIN_CREATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "institution": {"type": "string"},
        "role": {"type": "string", "enum": ["Admin", "Teacher", "Student"]},
    },
    "required": ["username", "password", "email", "institution", "role"],
}


UPLOAD_QUIZ_SCHEMA = {
  "type": "object",
  "properties": {
    "user_id": {"type": "integer"},
    "quiz_name": {
      "type": "string"
    },
    "questions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "question": {
            "type": "string"
          },
          "is_multichoice": {
            "type": "boolean"
          },
          "options": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "correct_option": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          },
          "is_mandatory": {
            "type": "boolean"
          },
          "marks": {
            "type": "integer"
          }
        },
        "required": ["question", "is_multichoice", "options", "correct_option", "is_mandatory", "marks"]
      }
    },
    "pass_marks": {
      "type": "integer"
    },
    "next_quiz_to_unlock": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    }
  },
  "required": ["quiz_name", "questions", "pass_marks", "next_quiz_to_unlock"]
}


SUBMIT_ANSWER_SCHEMA = {
  "type": "object",
  "properties": {
    "user_id": {"type": "integer"},
    "quiz_id": {
      "type": "integer"
    },
    "content": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "question_id": {
            "type": "integer"
          },
          "selected_options": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          }
        },
        "required": ["question_id", "selected_options"]
      }
    }
  },
  "required": ["quiz_id", "content"]
}
