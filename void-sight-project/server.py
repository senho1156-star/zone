from flask import Flask, request, jsonify
from flask_cors import CORS  # இதைச் சேர்க்கவும்

app = Flask(__name__)
CORS(app)  # இது Netlify-லிருந்து வரும் ரிக்வெஸ்ட்களை அனுமதிக்கிறது

# மற்ற கோடுகள் அப்படியே இருக்கும்...