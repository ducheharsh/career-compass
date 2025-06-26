from flask import Flask, request, jsonify
from flask_cors import CORS
from roadmap_gen.crew import RoadmapGen
from roadmap_gen.main import DEFAULT_INPUTS, RoadmapGenError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200

@app.route('/api/roadmap', methods=['POST'])
def generate_roadmap():
    """
    Generate a career roadmap based on the provided input.
    
    Expected JSON input:
    {
        "current_job_title": str,
        "current_salary": str,
        "current_job_market": str,
        "desired_job_title": str,
        "desired_salary": str,
        "desired_job_market": str,
        "current_industry": str,
        "desired_industry": str,
        "current_job_function": str,
        "desired_job_function": str,
        "current_skill_set": list[str],
        "desired_skill_set": list[str],
        "current_level_of_experience": str,
        "desired_level_of_experience": str,
        "current_location": str,
        "desired_location": str,
        "current_level_of_education": str,
        "desired_level_of_education": str
    }
    """
    try:
        # Get input data from request
        data = request.get_json()
        
        # Validate required fields
        required_fields = [
            "current_job_title", "current_salary", "current_job_market",
            "desired_job_title", "desired_salary", "desired_job_market",
            "current_industry", "desired_industry", "current_job_function",
            "desired_job_function", "current_skill_set", "desired_skill_set",
            "current_level_of_experience", "desired_level_of_experience",
            "current_location", "desired_location", "current_level_of_education",
            "desired_level_of_education"
        ]
        
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "error": f"Missing required field: {field}"
                }), 400
        
        # Generate roadmap
        crew = RoadmapGen().crew()
        result = crew.kickoff(inputs=data)
        
        # Read the generated files
        roadmap_md = ""
        roadmap_json = ""
        
        try:
            with open('roadmap.md', 'r') as f:
                roadmap_md = f.read()
        except FileNotFoundError:
            pass
            
        try:
            with open('roadmap.json', 'r') as f:
                roadmap_json = f.read()
        except FileNotFoundError:
            pass
        
        return jsonify({
            "status": "success",
            "result": result,
            "roadmap_md": roadmap_md,
            "roadmap_json": roadmap_json
        }), 200
        
    except RoadmapGenError as e:
        return jsonify({
            "error": str(e)
        }), 500
    except Exception as e:
        return jsonify({
            "error": f"An unexpected error occurred: {str(e)}"
        }), 500

def run_api():
    """Run the Flask API server."""
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)

if __name__ == '__main__':
    run_api() 