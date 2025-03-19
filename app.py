from flask import Flask
import subprocess
import datetime
import os
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = os.environ.get('USER', subprocess.getoutput('whoami'))
    
    full_name = "Sanjay JR"  
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    
    top_output = subprocess.getoutput('top -b -n 1')
    
    response = f"Name: {full_name}\n"
    response += f"user: {username}\n"
    response += f"Server Time (IST): {server_time}\n"
    response += f"TOP output:\n{top_output}"
    
    return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)