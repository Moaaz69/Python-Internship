import json
from status_tracker import create_feature_status_dict

def parse_requirements(file_path):
    project = timeline = priority = None
    features = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith("project:"):
                project = line.split(":", 1)[1].strip()
            elif line.lower().startswith("features:"):
                continue
            elif line.startswith("-"):
                features.append(line[1:].strip())
            elif line.lower().startswith("timeline:"):
                timeline = line.split(":", 1)[1].strip()
            elif line.lower().startswith("priority:"):
                priority = line.split(":", 1)[1].strip()
    return project, features, timeline, priority

def print_and_save_summary(project, features, timeline, priority, txt_file="project_summary.txt"):
    summary_lines = [
        "📘 Project Summary Report",
        "-------------------------",
        f"Project: {project}",
        f"Timeline: {timeline}",
        f"Priority: {priority}",
        "Features to Implement:"
    ]
    for feat in features:
        summary_lines.append(f"- {feat}")
    summary = "\n".join(summary_lines)
    print(summary)
       # Use utf-8 encoding here:
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(summary)

def export_to_json(project, features, timeline, priority, json_file="project_summary.json"):
    feature_status = create_feature_status_dict(features)
    data = {
        "Project": project,
        "Timeline": timeline,
        "Priority": priority,
        "Features": feature_status
    }
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    project, features, timeline, priority = parse_requirements("client_requirements.txt")
    print_and_save_summary(project, features, timeline, priority)
    export_to_json(project, features, timeline, priority)