#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from roadmap_gen.crew import RoadmapGen

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
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

    
    try:
        RoadmapGen().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
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

    try:
        RoadmapGen().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        RoadmapGen().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
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

    try:
        RoadmapGen().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
