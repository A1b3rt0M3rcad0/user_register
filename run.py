from src.main.server.server import Server

if __name__ == "__main__":
    server = Server()
    server.run(host="0.0.0.0", port=5000, debug=True)