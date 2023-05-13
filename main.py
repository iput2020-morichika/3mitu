from flask import Flask
from flask import render_template
app = Flask(__name__)

import test_dht11

@app.route('/')
def index():
    env = test_dht11.EnvSensorClass()
    temp, hum = env.GetTemp() # 温湿度を取得
    dht11 = {
      'temp' : temp,
      'hum' : hum
    }
    return render_template(
      'index.html',
      dht11 = dht11
      )

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
