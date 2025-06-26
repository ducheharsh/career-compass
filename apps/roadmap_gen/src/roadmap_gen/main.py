#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from roadmap_gen.crew import RoadmapGen

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Default input configuration for career transition analysis
DEFAULT_INPUTS = {
    "current_job_title": "Software Engineer",
    "current_salary": "₹8,00,000 per annum",
    "current_job_market": "IT Services",
    "desired_job_title": "Machine Learning Engineer",
    "desired_salary": "₹15,00,000 per annum",
    "desired_job_market": "AI & Data Science",
    "current_industry": "Software Development",
    "desired_industry": "Artificial Intelligence",
    "current_job_function": "Backend Development",
    "desired_job_function": "AI Model Development",
    "current_skill_set": ["Python", "Django", "SQL", "JavaScript"],
    "desired_skill_set": ["Python", "TensorFlow", "PyTorch", "ML Algorithms", "Data Engineering"],
    "current_level_of_experience": "3 years",
    "desired_level_of_experience": "5+ years",
    "current_location": "Bangalore, India",
    "desired_location": "Remote or Bangalore, India",
    "current_level_of_education": "Bachelor's in Computer Science",
    "desired_level_of_education": "Master's in AI & Machine Learning"
}

class RoadmapGenError(Exception):
    """Base exception class for RoadmapGen errors."""
    pass

def run():
    """
    Run the crew with default inputs.
    """
    try:
        RoadmapGen().crew().kickoff(inputs=DEFAULT_INPUTS)
    except Exception as e:
        raise RoadmapGenError(f"Failed to run crew: {str(e)}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    if len(sys.argv) < 3:
        raise RoadmapGenError("Missing required arguments: n_iterations and filename")
    
    try:
        n_iterations = int(sys.argv[1])
        filename = sys.argv[2]
        RoadmapGen().crew().train(n_iterations=n_iterations, filename=filename, inputs=DEFAULT_INPUTS)
    except ValueError:
        raise RoadmapGenError("Invalid number of iterations provided")
    except Exception as e:
        raise RoadmapGenError(f"Failed to train crew: {str(e)}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    if len(sys.argv) < 2:
        raise RoadmapGenError("Missing required argument: task_id")
    
    try:
        RoadmapGen().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise RoadmapGenError(f"Failed to replay crew: {str(e)}")

def test():
    """
    Test the crew execution and returns the results.
    """
    if len(sys.argv) < 3:
        raise RoadmapGenError("Missing required arguments: n_iterations and openai_model_name")
    
    try:
        n_iterations = int(sys.argv[1])
        openai_model_name = sys.argv[2]
        RoadmapGen().crew().test(n_iterations=n_iterations, openai_model_name=openai_model_name, inputs=DEFAULT_INPUTS)
    except ValueError:
        raise RoadmapGenError("Invalid number of iterations provided")
    except Exception as e:
        raise RoadmapGenError(f"Failed to test crew: {str(e)}")
