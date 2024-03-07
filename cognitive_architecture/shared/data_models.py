"""Data models for the cognitive architecture."""
from enum import Enum
from typing import Optional, List, Union
from pydantic import BaseModel, Field


class Node(BaseModel):
    """Node in a knowledge graph."""
    id: int
    description: str
    category: str
    color: str = "blue"
    memory_type: str
    created_at: Optional[float] = None
    summarized: Optional[bool] = None


class Edge(BaseModel):
    """Edge in a knowledge graph."""
    source: int
    target: int
    description: str
    color: str = "blue"
    created_at: Optional[float] = None
    summarized: Optional[bool] = None


class KnowledgeGraph(BaseModel):
    """Knowledge graph."""
    nodes: List[Node] = Field(..., default_factory=list)
    edges: List[Edge] = Field(..., default_factory=list)


class GraphQLQuery(BaseModel):
    """GraphQL query."""
    query: str


class MemorySummary(BaseModel):
    """ Memory summary. """
    nodes: List[Node] = Field(..., default_factory=list)
    edges: List[Edge] = Field(..., default_factory=list)



class TextSubclass(str, Enum):
    ARTICLES = "Articles, essays, and reports"
    BOOKS = "Books and manuscripts"
    NEWS_STORIES = "News stories and blog posts"
    RESEARCH_PAPERS = "Research papers and academic publications"
    SOCIAL_MEDIA = "Social media posts and comments"
    WEBSITE_CONTENT = "Website content and product descriptions"
    PERSONAL_NARRATIVES = "Personal narratives and stories"
    SPREADSHEETS = "Spreadsheets and tables"
    FORMS = "Forms and surveys"
    DATABASES = "Databases and CSV files"
    SOURCE_CODE = "Source code in various programming languages"
    SHELL_SCRIPTS = "Shell commands and scripts"
    MARKUP_LANGUAGES = "Markup languages (HTML, XML)"
    STYLESHEETS = "Stylesheets (CSS) and configuration files (YAML, JSON, INI)"
    CHAT_TRANSCRIPTS = "Chat transcripts and messaging history"
    CUSTOMER_SERVICE_LOGS = "Customer service logs and interactions"
    CONVERSATIONAL_AI = "Conversational AI training data"
    TEXTBOOK_CONTENT = "Textbook content and lecture notes"
    EXAM_QUESTIONS = "Exam questions and academic exercises"
    E_LEARNING_MATERIALS = "E-learning course materials"
    POETRY = "Poetry and prose"
    SCRIPTS = "Scripts for plays, movies, and television"
    SONG_LYRICS = "Song lyrics"
    MANUALS = "Manuals and user guides"
    TECH_SPECS = "Technical specifications and API documentation"
    HELPDESK_ARTICLES = "Helpdesk articles and FAQs"
    LEGAL_CONTRACTS = "Contracts and agreements"
    LAWS = "Laws, regulations, and legal case documents"
    POLICY_DOCUMENTS = "Policy documents and compliance materials"
    CLINICAL_TRIALS = "Clinical trial reports"
    PATIENT_RECORDS = "Patient records and case notes"
    SCIENTIFIC_ARTICLES = "Scientific journal articles"
    FINANCIAL_REPORTS = "Financial reports and statements"
    BUSINESS_PLANS = "Business plans and proposals"
    MARKET_RESEARCH = "Market research and analysis reports"
    AD_COPIES = "Ad copies and marketing slogans"
    PRODUCT_CATALOGS = "Product catalogs and brochures"
    PRESS_RELEASES = "Press releases and promotional content"
    PROFESSIONAL_EMAILS = "Professional and formal correspondence"
    PERSONAL_EMAILS = "Personal emails and letters"
    IMAGE_CAPTIONS = "Image and video captions"
    ANNOTATIONS = "Annotations and metadata for various media"
    VOCAB_LISTS = "Vocabulary lists and grammar rules"
    LANGUAGE_EXERCISES = "Language exercises and quizzes"

class AudioSubclass(str, Enum):
    MUSIC_TRACKS = "Music tracks and albums"
    PODCASTS = "Podcasts and radio broadcasts"
    AUDIOBOOKS = "Audiobooks and audio guides"
    INTERVIEWS = "Recorded interviews and speeches"
    SOUND_EFFECTS = "Sound effects and ambient sounds"

class ImageSubclass(str, Enum):
    PHOTOGRAPHS = "Photographs and digital images"
    ILLUSTRATIONS = "Illustrations, diagrams, and charts"
    INFOGRAPHICS = "Infographics and visual data representations"
    ARTWORK = "Artwork and paintings"
    SCREENSHOTS = "Screenshots and graphical user interfaces"

class VideoSubclass(str, Enum):
    MOVIES = "Movies and short films"
    DOCUMENTARIES = "Documentaries and educational videos"
    TUTORIALS = "Video tutorials and how-to guides"
    ANIMATED_FEATURES = "Animated features and cartoons"
    LIVE_EVENTS = "Live event recordings and sports broadcasts"

class MultimediaSubclass(str, Enum):
    WEB_CONTENT = "Interactive web content and games"
    VR_EXPERIENCES = "Virtual reality (VR) and augmented reality (AR) experiences"
    MIXED_MEDIA = "Mixed media presentations and slide decks"
    E_LEARNING_MODULES = "E-learning modules with integrated multimedia"
    DIGITAL_EXHIBITIONS = "Digital exhibitions and virtual tours"

class Model3DSubclass(str, Enum):
    ARCHITECTURAL_RENDERINGS = "Architectural renderings and building plans"
    PRODUCT_MODELS = "Product design models and prototypes"
    ANIMATIONS = "3D animations and character models"
    SCIENTIFIC_VISUALIZATIONS = "Scientific simulations and visualizations"
    VR_OBJECTS = "Virtual objects for AR/VR applications"

class ProceduralSubclass(str, Enum):
    TUTORIALS_GUIDES = "Tutorials and step-by-step guides"
    WORKFLOW_DESCRIPTIONS = "Workflow and process descriptions"
    SIMULATIONS = "Simulation and training exercises"
    RECIPES = "Recipes and crafting instructions"
class ContentType(BaseModel):
    """Base class for different types of content."""
    type: str

class TextContent(ContentType):
    type:str = "TEXT"
    subclass: List[TextSubclass]

class AudioContent(ContentType):
    type:str = "AUDIO"
    subclass: List[AudioSubclass]

class ImageContent(ContentType):
    type:str = "IMAGE"
    subclass: List[ImageSubclass]

class VideoContent(ContentType):
    type:str = "VIDEO"
    subclass: List[VideoSubclass]

class MultimediaContent(ContentType):
    type:str = "MULTIMEDIA"
    subclass: List[MultimediaSubclass]

class Model3DContent(ContentType):
    type:str = "3D_MODEL"
    subclass: List[Model3DSubclass]

class ProceduralContent(ContentType):
    type:str = "PROCEDURAL"
    subclass: List[ProceduralSubclass]

class ContentPrediction(BaseModel):
    """Class for a single class label prediction."""

    label: Union[TextContent, AudioContent, ImageContent, VideoContent, MultimediaContent, Model3DContent, ProceduralContent]


class CognitiveLayerSubgroup(BaseModel):
    """ CognitiveLayerSubgroup in a general layer """
    id: int
    name:str
    description: str


class CognitiveLayer(BaseModel):
    """Cognitive  layer"""
    category_name:str
    cognitive_layers: List[CognitiveLayerSubgroup] = Field(..., default_factory=list)

