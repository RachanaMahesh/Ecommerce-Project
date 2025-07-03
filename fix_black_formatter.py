import os
import sys
import subprocess
import json

def get_black_path():
    try:
        result = subprocess.run(["where", "black"], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            return result.stdout.strip().splitlines()[0]
        else:
            return None
    except Exception as e:
        print(f"Error locating Black: {e}")
        return None

def get_python_path():
    return sys.executable.replace("\\", "/")

def create_vscode_settings(project_root, black_path):
    vscode_dir = os.path.join(project_root, ".vscode")
    os.makedirs(vscode_dir, exist_ok=True)

    settings = {
        "editor.formatOnSave": True,
        "[python]": {
            "editor.defaultFormatter": "ms-python.python"
        },
        "python.formatter.provider": "black",
        "python.formatter.blackPath": black_path.replace("\\", "/")
    }

    settings_path = os.path.join(vscode_dir, "settings.json")
    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=4)
    print(f"✅ settings.json created at {settings_path}")

def create_pyproject_toml(project_root):
    content = """
[tool.black]
line-length = 88
target-version = ['py311']
skip-string-normalization = false
""".strip()

    toml_path = os.path.join(project_root, "pyproject.toml")
    with open(toml_path, "w") as f:
        f.write(content)
    print(f"✅ pyproject.toml created at {toml_path}")

def main():
    project_root = os.getcwd()
    black_path = get_black_path()
    if not black_path:
        print("❌ Black is not installed in this environment.")
        print("Install it using: pip install black")
        return

    print(f"✅ Found Black at: {black_path}")
    print(f"✅ Active Python interpreter: {get_python_path()}")

    create_vscode_settings(project_root, black_path)
    create_pyproject_toml(project_root)

    print("\n🎉 Done! Now reload VS Code and try formatting your Python file.")

if __name__ == "__main__":
    main()
