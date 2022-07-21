from operator import index
from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import CourseLesson, Progress, Quiz, QuizSubmissions, User
from models import Content
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db: List[User] = [
    
]

db2: List[Content] = [
    Content(
        id = uuid4(),
        topic = "android",
        name = "android1",
        url = "https://learn-world.s3.amazonaws.com/android1.mp4",
        type = "video"
    ),
    Quiz(
        id = uuid4(),
        type = "quiz",
        content_id = "3945f0e2-8b0a-49d9-b235-cf6027ad5843",
        name = "Android installation",
        question =  "Which one of the below is a View Group in Android?",
        options =  ["Text View", "Button", "Linear Layout", "Edit Text"],
        answer =  "Linear Layout",
        wrongAnsExplanation = ["This is a View in Android", "This is a View in Android", "correct", "This is a View in Android"]
    ),
    Content(
        id = uuid4(),
        name = "android2",
        topic = "android",
        url = "https://learn-world.s3.amazonaws.com/android2.mp4",
        type = "video"
    ),
    Content(
        id = uuid4(),
        name = "android Installation",
        topic = "android",
        url = "https://learn-world.s3.amazonaws.com/ISA-+Revised+-+NJ+-+30+May+2020+V1+prefinal.pdf",
        type = "pdf"
    ),
    Content(
        id = uuid4(),
        name = "android3",
        topic = "android",
        url = "https://learn-world.s3.amazonaws.com/android3.mp4",
        type = "video"
    ),
    Content(
        id = uuid4(),
        name = "android4",
        topic = "android",
        url = "https://learn-world.s3.amazonaws.com/android4.mp4",
        type = "video"
    ),
    Content(
        id = uuid4(),
        name = "android5",
        topic = "android",
        url = "https://learn-world.s3.amazonaws.com/android5.mp4",
        type = "video"
    ),
    Content(
        id = uuid4(),
        name = "android6",
        topic = "android",
        url = "https://learn-world.s3.amazonaws.com/android6.mp4",
        type = "video"
    ),
    Content(
        id = uuid4(),
        name = "android7",
        topic = "android",
        url = "https://learn-world.s3.amazonaws.com/android7.mp4",
        type = "video"
    ),
    Quiz(
        id = uuid4(),
        type = "quiz",
        content_id = "3945f0e2-8b0a-49d9-b235-cf6027ad5843",
        name = "Android installation",
        question =  "Which one of the below is a View Group in Android?",
        options =  ["Text View", "Button", "Linear Layout", "Edit Text"],
        answer =  "Linear Layout",
        wrongAnsExplanation = ["This is a View in Android", "This is a View in Android", "correct", "This is a View in Android"]
    ),
]

db3: List[Progress] = [
    
]

# db4: List[Quiz] = [
#     Quiz(
#         id = uuid4(),
#         content_id = "3945f0e2-8b0a-49d9-b235-cf6027ad5843",
#         question =  "Which one of the below is a View Group in Android?",
#         options =  "Text View, Button, Linear Layout, Edit Text ",
#         answer =  "Linear Layout",
#         wrongAnsExplanation = "This is a View in Android, This is a View in Android, correct, This is a View in Android"
#     ),
#     Quiz(
#         id = uuid4(),
#         content_id = "fd4c0755-e2c4-430d-b2f5-9d98551d48a8",
#         question =  "Which one of the below is a View Group in Android?",
#         options =  "Text View, Button, Linear Layout, Edit Text ",
#         answer =  "Linear Layout",
#         wrongAnsExplanation = "This is a View in Android, This is a View in Android, correct, This is a View in Android"
#     )
# ]

db5: List[QuizSubmissions] = [
    
]

db6: List[CourseLesson] = [
    CourseLesson(
        id = uuid4(),
        videos = [
            Content(
                id = uuid4(),
                topic = "android",
                name = "android1",
                url = "https://learn-world.s3.amazonaws.com/android1.mp4",
                type = "video"
            )
        ],
        topicName = "Android Studio installation",
        pdf = [
            Content(
                id = uuid4(),
                topic = "android",
                name = "android1",
                url = "https://learn-world.s3.amazonaws.com/ISA-+Revised+-+NJ+-+30+May+2020+V1+prefinal.pdf",
                type = "pdf"
            )
        ],
        quiz = [
            Quiz(
                id = uuid4(),
                type = "quiz",
                content_id = "3945f0e2-8b0a-49d9-b235-cf6027ad5843",
                name = "Android installation",
                question =  "Which one of the below is a View Group in Android?",
                options =  ["Text View", "Button", "Linear Layout", "Edit Text"],
                answer =  "Linear Layout",
                wrongAnsExplanation = ["This is a View in Android", "This is a View in Android", "correct", "This is a View in Android"]
            ),
        ]
    ),
    CourseLesson(
        id = uuid4(),
        videos = [
            Content(
                id = uuid4(),
                topic = "android",
                name = "android1",
                url = "https://learn-world.s3.amazonaws.com/android1.mp4",
                type = "video"
            )
        ],
        topicName = "Android Studio installation",
        pdf = [
            Content(
                id = uuid4(),
                topic = "android",
                name = "android1",
                url = "https://learn-world.s3.amazonaws.com/ISA-+Revised+-+NJ+-+30+May+2020+V1+prefinal.pdf",
                type = "pdf"
            )
        ],
        quiz = [
            Quiz(
                id = uuid4(),
                type = "quiz",
                content_id = "3945f0e2-8b0a-49d9-b235-cf6027ad5843",
                name = "Android installation",
                question =  "Which one of the below is a View Group in Android?",
                options =  ["Text View", "Button", "Linear Layout", "Edit Text"],
                answer =  "Linear Layout",
                wrongAnsExplanation = ["This is a View in Android", "This is a View in Android", "correct", "This is a View in Android"]
            ),
        ]
    ),
    CourseLesson(
        id = uuid4(),
        videos = [
            Content(
                id = uuid4(),
                topic = "android",
                name = "android1",
                url = "https://learn-world.s3.amazonaws.com/android1.mp4",
                type = "video"
            )
        ],
        topicName = "Android Studio installation",
        pdf = [
            Content(
                id = uuid4(),
                topic = "android",
                name = "android1",
                url = "https://learn-world.s3.amazonaws.com/ISA-+Revised+-+NJ+-+30+May+2020+V1+prefinal.pdf",
                type = "pdf"
            )
        ],
        quiz = [
            Quiz(
                id = uuid4(),
                type = "quiz",
                content_id = "3945f0e2-8b0a-49d9-b235-cf6027ad5843",
                name = "Android installation",
                question =  "Which one of the below is a View Group in Android?",
                options =  ["Text View", "Button", "Linear Layout", "Edit Text"],
                answer =  "Linear Layout",
                wrongAnsExplanation = ["This is a View in Android", "This is a View in Android", "correct", "This is a View in Android"]
            ),
        ]
    ),
    CourseLesson(
        id = uuid4(),
        videos = [
            Content(
                id = uuid4(),
                topic = "android",
                name = "android1",
                url = "https://learn-world.s3.amazonaws.com/android1.mp4",
                type = "video"
            )
        ],
        topicName = "Android Studio installation",
        pdf = [
            Content(
                id = uuid4(),
                topic = "android",
                name = "android1",
                url = "https://learn-world.s3.amazonaws.com/ISA-+Revised+-+NJ+-+30+May+2020+V1+prefinal.pdf",
                type = "pdf"
            )
        ],
        quiz = [
            Quiz(
                id = uuid4(),
                type = "quiz",
                content_id = "3945f0e2-8b0a-49d9-b235-cf6027ad5843",
                name = "Android installation",
                question =  "Which one of the below is a View Group in Android?",
                options =  ["Text View", "Button", "Linear Layout", "Edit Text"],
                answer =  "Linear Layout",
                wrongAnsExplanation = ["This is a View in Android", "This is a View in Android", "correct", "This is a View in Android"]
            ),
        ]
    ),
    CourseLesson(
        id = uuid4(),
        videos = [
            Content(
                id = uuid4(),
                topic = "android",
                name = "android1",
                url = "https://learn-world.s3.amazonaws.com/android1.mp4",
                type = "video"
            )
        ],
        topicName = "Android Studio installation",
        pdf = [
            Content(
                id = uuid4(),
                topic = "android",
                name = "android1",
                url = "https://learn-world.s3.amazonaws.com/ISA-+Revised+-+NJ+-+30+May+2020+V1+prefinal.pdf",
                type = "pdf"
            )
        ],
        quiz = [
            Quiz(
                id = uuid4(),
                type = "quiz",
                content_id = "3945f0e2-8b0a-49d9-b235-cf6027ad5843",
                name = "Android installation",
                question =  "Which one of the below is a View Group in Android?",
                options =  ["Text View", "Button", "Linear Layout", "Edit Text"],
                answer =  "Linear Layout",
                wrongAnsExplanation = ["This is a View in Android", "This is a View in Android", "correct", "This is a View in Android"]
            ),
        ]
    )
]

@app.get("/")


@app.get("/users")

async def fetch_users():
    return db

@app.post("/users")

async def register_user(user: User):
    db.append(user)
    return {"id": user.id }

@app.get("/content")

async def fetch_content():
    return db2

@app.get("/progress")

async def fetch_progress():
    return db3

@app.delete("/delete-progress")

async def delete_progress(id): 
    print(id)
    # lists = [x for x in db3 if x.user_id == "z3NiJa1NPafLgIsK5hzwCZSrVah1"]
    for item in db3:
        print(item)
        if item.user_id == id :
           db3.remove(item)

    return db3

@app.post("/add-progress")

async def register_user(progress: Progress):
    db3.append(progress)
    return {"id": progress.id }

# @app.get("/quiz")

# async def fetch_quiz():
#     return db4

@app.post("/quiz-submissions")

async def add_submission(submission: QuizSubmissions):
    db5.append(submission)
    return {"id": submission.id }

@app.get("/quiz-submissions")

async def fetch_progress():
    return db5


@app.get("/course-lesson")

async def fetch_course_lesson():
    return db6