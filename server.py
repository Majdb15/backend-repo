import os
import yaml

class Server:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
    
    def load_config(self, path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)
    
    def start(self):
        server_ip = self.config.get('ServerIPAddress', 'localhost')
        run_localhost = self.config.get('run_localhost', False)
        
        if run_localhost:
            print(f"Starting server on localhost with IP: {server_ip}")
        else:
            print(f"Starting server at {server_ip}")

if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')  # Adjust the path as needed
    server_instance = Server(config_path)
    server_instance.start()

##