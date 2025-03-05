import kagglehub

def main():
    update_dataset()
    

def update_dataset():
    # Download latest version
    path = kagglehub.dataset_download("ihelon/coffee-sales")

    print("Path to dataset files:", path)


if __name__ == '__main__':
    main()