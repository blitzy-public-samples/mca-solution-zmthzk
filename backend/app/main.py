from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from backend.app.api.routes import register_routes
from backend.app.core.config import settings
from backend.app.db.firestore import init_db
from backend.app.services.email_processor import init_email_processor
from backend.app.tasks.celery_tasks import celery_app

app = Flask(__name__)

def create_app():
    app.config.from_object(settings)
    
    CORS(app)
    JWTManager(app)
    
    init_db(app)
    register_routes(app)
    init_email_processor(app)
    
    # Configure error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Not found"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Internal server error"}, 500

    return app

# HUMAN ASSISTANCE NEEDED
# The following function has a confidence level below 0.8 and may need review
def configure_celery(app):
    celery_app.conf.update(app.config)

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask

if __name__ == "__main__":
    app = create_app()
    configure_celery(app)
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)