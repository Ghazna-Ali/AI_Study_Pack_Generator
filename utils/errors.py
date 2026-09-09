class StudyPackError(Exception):
    """Base application error."""


class AIServiceError(StudyPackError):
    """AI API failure."""


class ValidationError(StudyPackError):
    """AI output validation failure."""


class WorkflowError(StudyPackError):
    """Workflow execution failure."""


class ConfigurationError(StudyPackError):
    """Application configuration failure."""