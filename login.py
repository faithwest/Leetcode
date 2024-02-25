
@app.route("/admin/login", methods=["POST"])
def admin_login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": True, "message": "Invalid JSON data in request"}), 400

        email = data.get("email")
        password = data.get("password")

        # Fetch the user from the database by email
        admin = User.query.filter_by(email=email, role=User.ROLE_ADMIN).first()
        if admin:
            # Check if the provided password matches the hashed password in the database
            if bcrypt.check_password_hash(admin.password, password):
                return jsonify({"message": "Admin login successful."}), 200
            else:
                return jsonify({"error": True, "message": "Invalid password."}), 401
        else:
            return jsonify({"error": True, "message": "Admin not found."}), 401

    except Exception as e:
        return jsonify({"error": True, "message": f"An error occurred: {str(e)}"}), 500
