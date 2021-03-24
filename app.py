from client.index import app
import logging

logging.basicConfig(filename="Logservice.log",
                    filemode="a",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')

if __name__ == "__main__":
    app.run(debug=True)
