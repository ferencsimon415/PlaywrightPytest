import json
import csv
import yaml
import os
from typing import Dict, Any, List
from pathlib import Path

class DataLoader:
    def __init__(self, data_dir: str = "data"):
        self.base_path = Path(__file__).parent.parent.resolve()
        self.data_dir = os.path.join(self.base_path, data_dir)
        
    def load_json(self, filename: str) -> Dict[str, Any]:
        """Load data from JSON file"""
        file_path = os.path.join(self.data_dir, filename)
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {file_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in {filename}: {str(e)}")

    def load_yaml(self, filename: str) -> Dict[str, Any]:
        """Load data from YAML file"""
        file_path = os.path.join(self.data_dir, filename)
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"YAML file not found at {file_path}")

    def load_csv(self, filename: str) -> List[Dict[str, str]]:
        """Load data from CSV file and return as list of dictionaries"""
        file_path = os.path.join(self.data_dir, filename)
        try:
            with open(file_path, 'r') as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found at {file_path}")

    def get_test_data(self, dataset_name: str, data_file: str = "test_data.json") -> Any:
        """Get specific dataset from test data file"""
        data = self.load_json(data_file)
        return data.get(dataset_name, {})

    def get_environment_data(self, environment: str = "dev") -> Dict[str, Any]:
        """Load environment-specific configuration"""
        return self.load_yaml(f"config_{environment}.yaml")

# Example usage:
if __name__ == "__main__":
    loader = DataLoader()
    test_data = loader.load_json("test_data.json")
    config = loader.load_yaml("config_dev.yaml")