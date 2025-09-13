from flask import Flask, request, jsonify
from config import Config
from models import db, User, Workout
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime, timedelta
from sqlalchemy import func

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["JWT_SECRET_KEY"] = "supersecretkey"

    db.init_app(app)
    jwt = JWTManager(app)

    @app.route("/")
    def home():
        return {"msg": "Fitness Tracker Backend is running with Workouts!"}

    # -------- Register --------
    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json()
        user = User(
            name=data.get("name"),
            email=data.get("email"),
            age=data.get("age"),
            weight=data.get("weight")
        )
        user.set_password(data.get("password"))
        db.session.add(user)
        db.session.commit()
        return jsonify({"msg": "User registered successfully!", "user": user.to_dict()}), 201

    # -------- Login --------
    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        user = User.query.filter_by(email=data.get("email")).first()
        if not user or not user.check_password(data.get("password")):
            return jsonify({"msg": "Invalid email or password"}), 401
        token = create_access_token(identity=str(user.user_id)) 
        return jsonify({"msg": "Login successful", "access_token": token, "user": user.to_dict()}), 200

    # -------- Add Workout --------
    @app.route("/workouts", methods=["POST"])
    @jwt_required()
    def add_workout():
        try:
            user_id = int(get_jwt_identity())
            data = request.get_json()

            # Validate required fields
            if not all([data.get("date"), data.get("exercise_type"), data.get("duration"), data.get("calories")]):
                return jsonify({"msg": "All fields (date, exercise_type, duration, calories) are required"}), 400

            # Parse date safely
            try:
                workout_date = datetime.strptime(data.get("date"), "%Y-%m-%d").date()
            except ValueError:
                return jsonify({"msg": "Date must be in YYYY-MM-DD format"}), 400

            workout = Workout(
                user_id=user_id,
                date=workout_date,
                exercise_type=data.get("exercise_type"),
                duration=int(data.get("duration")),
                calories=float(data.get("calories"))
            )
            db.session.add(workout)
            db.session.commit()

            return jsonify({"msg": "Workout added!", "workout": workout.to_dict()}), 201

        except Exception as e:
            # This will show the exact error in your response instead of silent 500
            return jsonify({"error": str(e)}), 500


    # -------- Get Workouts --------
    @app.route("/workouts", methods=["GET"])
    @jwt_required()
    def get_workouts():
        user_id = int(get_jwt_identity())
        workouts = Workout.query.filter_by(user_id=user_id).all()
        return jsonify([w.to_dict() for w in workouts]), 200
   
    # -------- Edit Workout --------
    @app.route("/workouts/<int:workout_id>", methods=["PUT"])
    @jwt_required()
    def edit_workout(workout_id):
        user_id = int(get_jwt_identity())
        workout = Workout.query.filter_by(workout_id=workout_id, user_id=user_id).first()
        if not workout:
            return jsonify({"msg": "Workout not found"}), 404

        data = request.get_json()
        if "date" in data:
            workout.date = datetime.strptime(data.get("date"), "%Y-%m-%d").date()
        if "exercise_type" in data:
            workout.exercise_type = data.get("exercise_type")
        if "duration" in data:
            workout.duration = data.get("duration")
        if "calories" in data:
            workout.calories = data.get("calories")

        db.session.commit()
        return jsonify({"msg": "Workout updated!", "workout": workout.to_dict()}), 200

    # -------- Delete Workout --------
    @app.route("/workouts/<int:workout_id>", methods=["DELETE"])
    @jwt_required()
    def delete_workout(workout_id):
        user_id = int(get_jwt_identity())
        workout = Workout.query.filter_by(workout_id=workout_id, user_id=user_id).first()
        if not workout:
            return jsonify({"msg": "Workout not found"}), 404

        db.session.delete(workout)
        db.session.commit()
        return jsonify({"msg": "Workout deleted!"}), 200

    

    # -------- Progress: Weekly Calories --------
    @app.route("/progress/weekly", methods=["GET"])
    @jwt_required()
    def weekly_progress():
        user_id = int(get_jwt_identity())
        today = datetime.today().date()
        week_start = today - timedelta(days=today.weekday())  # Monday

        workouts = (
            db.session.query(Workout.exercise_type, func.sum(Workout.calories))
            .filter(Workout.user_id == user_id, Workout.date >= week_start)
            .group_by(Workout.exercise_type)
            .all()
        )

        result = [{"exercise_type": w[0], "calories": w[1]} for w in workouts]
        return jsonify({"week_start": str(week_start), "progress": result}), 200

    # -------- Progress: Monthly Calories --------
    @app.route("/progress/monthly", methods=["GET"])
    @jwt_required()
    def monthly_progress():
        user_id = int(get_jwt_identity())
        today = datetime.today().date()
        month_start = today.replace(day=1)

        workouts = (
            db.session.query(Workout.exercise_type, func.sum(Workout.calories))
            .filter(Workout.user_id == user_id, Workout.date >= month_start)
            .group_by(Workout.exercise_type)
            .all()
        )

        result = [{"exercise_type": w[0], "calories": w[1]} for w in workouts]
        return jsonify({"month_start": str(month_start), "progress": result}), 200

    # -------- Progress: Filtered by type/date range --------
    @app.route("/progress/filter", methods=["POST"])
    @jwt_required()
    def filter_progress():
        user_id = int(get_jwt_identity())
        data = request.get_json()

        start_date = data.get("start_date")  # "2025-09-01"
        end_date = data.get("end_date")      # "2025-09-12"
        exercise_type = data.get("exercise_type")

        query = Workout.query.filter_by(user_id=user_id)

        if start_date:
            query = query.filter(Workout.date >= datetime.strptime(start_date, "%Y-%m-%d").date())
        if end_date:
            query = query.filter(Workout.date <= datetime.strptime(end_date, "%Y-%m-%d").date())
        if exercise_type:
            query = query.filter(Workout.exercise_type == exercise_type)

        workouts = query.all()
        return jsonify([w.to_dict() for w in workouts]), 200



    # -------- Analytics --------
    @app.route("/analytics", methods=["GET"])
    @jwt_required()
    def analytics():
        user_id = int(get_jwt_identity())

        # Total calories per week
        today = datetime.today().date()
        week_start = today - timedelta(days=today.weekday())
        total_week = db.session.query(func.sum(Workout.calories)) \
            .filter(Workout.user_id == user_id, Workout.date >= week_start).scalar() or 0

        # Total calories per month
        month_start = today.replace(day=1)
        total_month = db.session.query(func.sum(Workout.calories)) \
            .filter(Workout.user_id == user_id, Workout.date >= month_start).scalar() or 0

        # Average duration per exercise type
        avg_duration = db.session.query(Workout.exercise_type, func.avg(Workout.duration)) \
            .filter(Workout.user_id == user_id) \
            .group_by(Workout.exercise_type).all()
        avg_duration_result = [{"exercise_type": t[0], "avg_duration": float(t[1])} for t in avg_duration]

        # Max calories burned in single workout
        max_calories = db.session.query(func.max(Workout.calories)) \
            .filter(Workout.user_id == user_id).scalar() or 0

        return jsonify({
            "total_week_calories": total_week,
            "total_month_calories": total_month,
            "avg_duration_per_exercise": avg_duration_result,
            "max_calories_single_workout": max_calories
        })

    # -------- Update User Profile --------
    @app.route("/user", methods=["PUT"])
    @jwt_required()
    def update_user():
        user_id = int(get_jwt_identity())
        user = User.query.get(user_id)
        if not user:
            return jsonify({"msg": "User not found"}), 404

        data = request.get_json()
        if "name" in data:
            user.name = data["name"]
        if "age" in data:
            user.age = data["age"]
        if "weight" in data:
            user.weight = data["weight"]
        if "password" in data:
            user.set_password(data["password"])

        db.session.commit()
        return jsonify({"msg": "Profile updated successfully", "user": user.to_dict()})

    # -------- Centralized Error Handler --------
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error": "Bad Request", "msg": str(e)}), 400

    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({"error": "Unauthorized", "msg": str(e)}), 401

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not Found", "msg": str(e)}), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error": "Internal Server Error", "msg": str(e)}), 500


    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)


