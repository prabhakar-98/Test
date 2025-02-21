from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Prabhakar Mandal" 
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    
    # Get IST time
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    
    # Get 'top' command output
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -10", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    return f"""
    <html>
        <head><title>System Info</title></head>
        <body>
            <h1>System Info</h1>
            <p><b>Name:</b> {name}</p>
            <p><b>Username:</b> {username}</p>
            <p><b>Server Time (IST):</b> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


