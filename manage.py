
from app import create_app
from flask_script import Manager, Server

# Creating app instance
app = create_app("development")

manager = Manager(app)
FLASK_RUN_PORT=8000
manager.add_command("server", Server)

if __name__ == "__main__":
    manager.run()
