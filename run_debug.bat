@echo on
start cmd /k "cd backend && set FLASK_APP=app && set FLASK_ENV=development && flask init-db && flask run"

@echo on
start cmd /k "cd frontend && npm run serve"