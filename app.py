from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary storage (for demo only)
vendors = []

# -----------------------
# Signup Route
# -----------------------
@app.route('/signup', methods=['POST']) # @=> This is a decorator. app route tells to use this function
def signup():
    data = request.json      #login() function

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Hash password
    hashed_password = generate_password_hash(password)

    # Store vendor
    vendor = {
        "name": name,
        "email": email,
        "password": hashed_password
    }

    vendors.append(vendor)

    return jsonify({"message": "Vendor registered successfully"})


# -----------------------
# Login Route
# -----------------------
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Find vendor
    for vendor in vendors:
        if vendor["email"] == email:
            if check_password_hash(vendor["password"], password):
                return jsonify({"message": "Login successful"})
            else:
                return jsonify({"message": "Invalid password"}), 401

    return jsonify({"message": "Vendor not found"}), 404


# -----------------------
# Run Server
# -----------------------
if __name__ == '__main__':
    app.run(debug=True)


    #Loan application route
    @app.route('/apply-loan',methods =['POST'])
    def apply_loan():
        data = request.json

        required_fields = ["name","aadhar","pan","annual_income","scheme_type"]
        #Check if all required fields exist
        for field in required_fields:
            if not data.get(field):
                return jsonify({"error":f"{field} is required"}),400
            
            #Validate Aadhar(12 Digits)
            if not data["aadhar"].isdigit() or len(data["aadhar"]) != 12:
                return jsonify({"error": "Invalid Aadhar Number"}),400
            
            #Validate PAN(simple format check)
            if len(data["pan"]) != 10:
                return jsonify({"error": "Invalid PAN Number"}),400
            
            #Validate income eligibility
            if float(data["annual_income"]) < 200000:
                return jsonify({"error":"Income below eligibility criteria"}),400
            
            return jsonify({"message": "Loan application submitted completely"})
        
      
