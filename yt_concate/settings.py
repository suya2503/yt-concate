from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
# video_file_output_path
VIDEOS_DIR = os.path.join(ROOT_DIR, 'downloads', 'videos')
# caption_output_path
CAPTIONS_DIR = os.path.join(ROOT_DIR, 'downloads', 'captions')
