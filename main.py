from indoor_location_system.indoor_location import IndoorLocationSystem
from image_recognition.image_recognition import ImageRecognitionSystem
from locaBD.database_manager import DatabaseManager

class SmartSystem:
    def __init__(self):
        self.location_system = IndoorLocationSystem(access_points)
        self.image_recognition_system = ImageRecognitionSystem(model_path)
        self.database_manager = DatabaseManager(db_path)

    def start (self):
        captured_image = capture_image()
        identified_objects = self.image_recognition_system.identify_objects(captured_image)

        wifi_signals = get_wifi_signals()
        estimated_position = self.location_system.estimate_position(wifi_signals)

        nearby_products = self.database_manager.get_nearby_products(estimated_position, identified_objects)

        # Usar as informações coletadas para interagir com o usuário ou realizar outras ações

if __name__ == "__main__":
    smart_system = SmartSystem()
    smart_system.start()