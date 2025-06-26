# RoadmapGen Crew

Welcome to the RoadmapGen Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
pip install -e .
```

### Configuration

1. Create a `.env` file in the project root with the following variables:
```env
# Flask Configuration
PORT=5000
FLASK_DEBUG=True

# OpenAI Configuration
OPENAI_API_KEY=your-api-key-here

# CrewAI Configuration
CREWAI_VERBOSE=True
```

2. Replace `your-api-key-here` with your actual OpenAI API key.

## Running the Project

### CLI Mode

To run the roadmap generation in CLI mode:

```bash
python -m roadmap_gen.main
```

### API Mode

To start the Flask API server:

```bash
# Using the installed command
roadmap_gen api

# Or with custom options
roadmap_gen api --port 8080 --debug
```

The API will be available at `http://localhost:5000` (or your specified port) with the following endpoints:

1. Health Check:
```bash
curl http://localhost:5000/health
```

2. Generate Roadmap:
```bash
curl -X POST http://localhost:5000/api/roadmap \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

The API will return a JSON response with:
- `status`: Success or error status
- `result`: The crew execution result
- `roadmap_md`: The generated roadmap in Markdown format
- `roadmap_json`: The generated roadmap in React Flow JSON format

## Development

To run the project in development mode:

1. Install development dependencies:
```bash
pip install -e ".[dev]"
```

2. Run the API server with debug mode:
```bash
roadmap_gen api --debug
```

## Customizing

- Modify `src/roadmap_gen/config/agents.yaml` to define your agents
- Modify `src/roadmap_gen/config/tasks.yaml` to define your tasks
- Modify `src/roadmap_gen/crew.py` to add your own logic, tools and specific args
- Modify `src/roadmap_gen/main.py` to add custom inputs for your agents and tasks
- Modify `src/roadmap_gen/api.py` to customize the API endpoints and behavior
- Modify `src/roadmap_gen/cli.py` to add new CLI commands

## Understanding Your Crew

The roadmap-gen Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the RoadmapGen Crew or crewAI:
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
