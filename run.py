from hell import create_app
import os
port_1 = int(os.environ["PORT"])

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port_1, debug=True)
