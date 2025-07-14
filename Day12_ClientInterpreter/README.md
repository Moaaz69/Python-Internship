           ****Client Requirements Interpreter****

This Python CLI tool reads and summarizes client requirements from a structured text file.
It extracts the project name, features, timeline, and priority, then outputs a formatted summary to both the console and a text file.
Features are also tracked with status and exported to a JSON file for further processing.

Key Features:

1) Parses and summarizes client requirements from client_requirements.txt
2) Outputs a clean summary to the console and project_summary.txt
3) Tracks feature statuses using a separate module (status_tracker.py)
4) Exports all project data and feature statuses to project_summary.json
5) Modular code structure for easy maintenance and extension