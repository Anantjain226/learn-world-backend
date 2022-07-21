from typing import List, Optional, Union
from uuid import UUID, uuid4
from xmlrpc.client import boolean
from pydantic import BaseModel

class User(BaseModel): 
    id: Optional[UUID] = uuid4()
    name: str
    email: str
    
class Content(BaseModel):
    id: Optional[UUID] = uuid4()
    topic: str
    name: str
    url: str
    type: str

class Progress(BaseModel):
    id: Optional[UUID] = uuid4()
    completed: bool
    content_id: str
    user_id: str
    type: str

class Quiz(BaseModel):
    id: Optional[UUID] = uuid4()
    type: str
    question: str
    name: str
    options: list
    answer: str
    wrongAnsExplanation: list

class QuizSubmissions(BaseModel):
    id: Optional[UUID] = uuid4()
    quiz_id: str
    user_id: str
    isCorrect: bool

class CourseLesson(BaseModel):
    id: Optional[UUID] = uuid4()
    videos: list[Content]
    topicName: str
    pdf: List[Content]
    quiz: list[Quiz]