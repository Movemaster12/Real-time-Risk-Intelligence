import requests, shutil, os.path

def download_data(url = "https://github.com/Movemaster12/Real-time-Risk-Intelligence/releases/download/pre-release/creditcard.csv"):
    # Download dataset and move to the right folder
    if not os.path.isfile("data/raw/creditcard.csv"):
        response = requests.get(url).content
        file = open("creditcard.csv", "wb")
        file.write(response)
        file.close()
        source = "creditcard.csv"
        dst = "data/raw/"
        shutil.move(source, dst)    

if __name__ == "__main__":
    download_data()