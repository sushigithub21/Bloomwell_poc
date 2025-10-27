from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/prescriptions', methods=['GET'])
def get_prescriptions():
       prescriptions = [
           {
               "prescription_id": "RX001",
               "patient_id": "P001",
               "status": "PENDING",
               "created_at": "2025-10-25T09:00:00Z",
               "modified_at": "2025-10-25T09:00:00Z"
           },
           {
               "prescription_id": "RX002",
               "patient_id": "P002",
               "status": "FILLED",
               "created_at": "2025-10-25T09:15:00Z",
               "modified_at": "2025-10-25T09:30:00Z"
           }
       ]
       return jsonify(prescriptions)

@app.route('/prescriptions/modified', methods=['GET'])
def get_modified_prescriptions():
       modified_prescriptions = [
           {
               "prescription_id": "RX001",
               "patient_id": "P001",
               "status": "DELIVERED",
               "created_at": "2025-10-25T09:00:00Z",
               "modified_at": "2025-10-26T11:00:00Z"
           }
       ]
       return jsonify(modified_prescriptions)

if __name__ == '__main__':
       app.run(debug=True)