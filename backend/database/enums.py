from enum import Enum


class Sex(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
    PREFER_NOT_TO_SAY = "Prefer Not To Say"


class Sport(str, Enum):
    RUNNING = "Running"
    CYCLING = "Cycling"
    TRIATHLON = "Triathlon"
    SWIMMING = "Swimming"
    ROWING = "Rowing"
    STRENGTH = "Strength"
    CROSSFIT = "CrossFit"
    HYROX = "Hyrox"
    OTHER = "Other"


class ExperienceLevel(str, Enum):
    BEGINNER = "Beginner"
    NOVICE = "Novice"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    ELITE = "Elite"
    PROFESSIONAL = "Professional"


class InjuryStatus(str, Enum):
    HEALTHY = "Healthy"
    MINOR = "Minor"
    RECOVERING = "Recovering"
    INJURED = "Injured"


class GoalCategory(str, Enum):
    ENDURANCE = "Endurance"
    STRENGTH = "Strength"
    SPEED = "Speed"
    POWER = "Power"
    WEIGHT_LOSS = "Weight Loss"
    BODY_COMPOSITION = "Body Composition"
    GENERAL_FITNESS = "General Fitness"
    OTHER = "Other"


class GoalStatus(str, Enum):
    NOT_STARTED = "Not Started"
    ACTIVE = "Active"
    PAUSED = "Paused"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class TrainingType(str, Enum):
    EASY = "Easy"
    RECOVERY = "Recovery"
    LONG = "Long"
    TEMPO = "Tempo"
    THRESHOLD = "Threshold"
    INTERVAL = "Interval"
    HILL = "Hill"
    RACE = "Race"
    STRENGTH = "Strength"
    MOBILITY = "Mobility"
    REST = "Rest"


class WorkoutIntensity(str, Enum):
    VERY_EASY = "Very Easy"
    EASY = "Easy"
    MODERATE = "Moderate"
    HARD = "Hard"
    VERY_HARD = "Very Hard"
    MAXIMAL = "Maximal"


class RecoveryStatus(str, Enum):
    EXCELLENT = "Excellent"
    GOOD = "Good"
    FAIR = "Fair"
    POOR = "Poor"
    VERY_POOR = "Very Poor"


class RecommendationType(str, Enum):
    REST = "Rest"
    RECOVERY = "Recovery"
    EASY_RUN = "Easy Run"
    LONG_RUN = "Long Run"
    TEMPO = "Tempo"
    INTERVAL = "Interval"
    STRENGTH = "Strength"
    MOBILITY = "Mobility"
    CROSS_TRAIN = "Cross Train"


class PerformanceCycleStatus(str, Enum):
    PLANNED = "Planned"
    ACTIVE = "Active"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
