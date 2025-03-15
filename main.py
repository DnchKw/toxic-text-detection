import uvicorn
from backend.app import app
from utils.nltk_download import download

def main():
    download()
    uvicorn.run(app)


if __name__ == "__main__":
    main()
