import pprint


def main():
    dataset = get_dataset()
    

def get_dataset():
    import kagglehub

    # Download latest version
    path = kagglehub.dataset_download("ihelon/coffee-sales")

    print("Path to dataset files:", path)

if __name__ == '__main__':
    main()